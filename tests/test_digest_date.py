"""Digest filenames follow the Asia/Shanghai calendar, including overnight."""

import asyncio
import re
from datetime import datetime, timezone
from pathlib import Path

import pytest

from src.digest_date import digest_calendar_date, digest_date_str
from src.models import (
    AIConfig,
    ClassificationResult,
    Config,
    ContentAnalysis,
    ContentItem,
    ProcessingResult,
    SourceType,
    SourcesConfig,
)
from src.orchestrator import HorizonOrchestrator
from src.processing.history import HistorySearchTool
from src.storage.manager import StorageManager


ROOT = Path(__file__).resolve().parents[1]
# 16:30 UTC is 00:30 the next calendar day in Asia/Shanghai.
OVERNIGHT_UTC = datetime(2026, 11, 16, 16, 30, tzinfo=timezone.utc)
SHANGHAI_TODAY = "2026-11-17"
UTC_TODAY = "2026-11-16"


class _FrozenDateTime(datetime):
    @classmethod
    def now(cls, tz=None):
        if tz is None:
            return OVERNIGHT_UTC
        return OVERNIGHT_UTC.astimezone(tz)


def _freeze_digest_clock(monkeypatch) -> None:
    monkeypatch.setattr("src.digest_date.datetime", _FrozenDateTime)


def test_digest_date_uses_asia_shanghai_across_the_utc_boundary() -> None:
    assert digest_date_str(datetime(2026, 11, 16, 15, 59, tzinfo=timezone.utc)) == UTC_TODAY
    assert digest_calendar_date(OVERNIGHT_UTC).isoformat() == SHANGHAI_TODAY
    assert digest_date_str(OVERNIGHT_UTC) == SHANGHAI_TODAY
    # 00:00 UTC is 08:00 Asia/Shanghai on the same calendar date.
    same_morning = datetime(2026, 11, 17, 0, 0, tzinfo=timezone.utc)
    assert digest_date_str(same_morning) == SHANGHAI_TODAY


def test_digest_date_rejects_a_naive_datetime() -> None:
    with pytest.raises(ValueError):
        digest_date_str(datetime(2026, 11, 17, 0, 17))


def test_daily_summary_runs_every_day_and_dates_pages_in_shanghai() -> None:
    text = (ROOT / ".github/workflows/daily-summary.yml").read_text(encoding="utf-8")
    crons = re.findall(r"cron: '([^']+)'", text)
    assert crons == [
        "17 0 * * *",
        "52 8 * * *",
        "17 12 * * *",
        "23 15 * * *",
    ]
    assert text.count('timezone: "Asia/Shanghai"') == 4
    assert "1-5" not in text
    assert "utc_today" not in text
    assert "_posts/${shanghai_today}-summary-${lang}.md" in text
    assert "DATE=$(TZ=Asia/Shanghai date +'%Y-%m-%d')" in text
    assert "cancel-in-progress: false" in text
    assert "group: daily-horizon-summary" in text


def _item() -> ContentItem:
    return ContentItem(
        id="rss:example:atlas",
        source_type=SourceType.RSS,
        title="Atlas",
        url="https://example.com/atlas",
        published_at=OVERNIGHT_UTC,
        processing=ProcessingResult(
            classification=ClassificationResult(profile="tech-news", method="source_override"),
            analysis=ContentAnalysis(score=9.0, reason="test", summary="Atlas"),
        ),
    )


class _Summarizer:
    def __init__(self, **kwargs):  # type: ignore[no-untyped-def]
        del kwargs

    async def generate_summary(self, items, date, total_fetched, language="en"):  # type: ignore[no-untyped-def]
        del items, total_fetched
        return f"# Horizon Daily - {date}\n\n{language} body\n"


class _FailureNotifier:
    def __init__(self) -> None:
        self.dates: list[str] = []

    async def send_failure(self, date: str, error_message: str) -> None:
        del error_message
        self.dates.append(date)


def test_pages_posts_use_shanghai_date_when_utc_is_still_yesterday(tmp_path, monkeypatch) -> None:
    _freeze_digest_clock(monkeypatch)
    config = Config(
        ai=AIConfig(
            provider="openai",
            model="test",
            api_key_env="TEST_API_KEY",
            languages=["zh", "en"],
        ),
        sources=SourcesConfig(),
    )
    storage = StorageManager(str(tmp_path / "data"))
    orchestrator = HorizonOrchestrator(config, storage)
    monkeypatch.chdir(tmp_path)
    seen_dates: list[str] = []

    class RecordingSummarizer(_Summarizer):
        async def generate_summary(self, items, date, total_fetched, language="en"):  # type: ignore[no-untyped-def]
            seen_dates.append(date)
            return await super().generate_summary(items, date, total_fetched, language)

    async def fetch_all_sources(since):  # type: ignore[no-untyped-def]
        del since
        return [_item()]

    async def analyze_items(items):  # type: ignore[no-untyped-def]
        return items

    async def merge_topic_duplicates(items, *, log=True):  # type: ignore[no-untyped-def]
        del log
        return items

    async def expand_twitter_discussion(items):  # type: ignore[no-untyped-def]
        del items

    async def enrich_items(items):  # type: ignore[no-untyped-def]
        del items

    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)
    monkeypatch.setattr(orchestrator, "analyze_items", analyze_items)
    monkeypatch.setattr(orchestrator, "merge_topic_duplicates", merge_topic_duplicates)
    monkeypatch.setattr(orchestrator, "_expand_twitter_discussion", expand_twitter_discussion)
    monkeypatch.setattr(orchestrator, "enrich_items", enrich_items)
    monkeypatch.setattr("src.orchestrator.DailySummarizer", RecordingSummarizer)

    asyncio.run(orchestrator.run())

    assert seen_dates == [SHANGHAI_TODAY, SHANGHAI_TODAY]
    for language in ("zh", "en"):
        post = tmp_path / "docs" / "_posts" / f"{SHANGHAI_TODAY}-summary-{language}.md"
        text = post.read_text(encoding="utf-8")
        assert f"date: {SHANGHAI_TODAY}" in text
        assert f"lang: {language}" in text
        summary = tmp_path / "data" / "summaries" / f"horizon-{SHANGHAI_TODAY}-{language}.md"
        assert summary.exists()
        assert not (tmp_path / "docs" / "_posts" / f"{UTC_TODAY}-summary-{language}.md").exists()


def test_failure_notice_uses_shanghai_date(tmp_path, monkeypatch) -> None:
    _freeze_digest_clock(monkeypatch)
    config = Config(
        ai=AIConfig(
            provider="openai",
            model="test",
            api_key_env="TEST_API_KEY",
            languages=["en"],
        ),
        sources=SourcesConfig(),
    )
    orchestrator = HorizonOrchestrator(config, StorageManager(str(tmp_path / "data")))
    notifier = _FailureNotifier()
    orchestrator.webhook_notifier = notifier
    orchestrator.wechat_notifier = notifier

    async def fetch_all_sources(since):  # type: ignore[no-untyped-def]
        del since
        raise RuntimeError("fetch failed")

    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)

    with pytest.raises(RuntimeError, match="fetch failed"):
        asyncio.run(orchestrator.run())

    assert notifier.dates == [SHANGHAI_TODAY, SHANGHAI_TODAY]


def test_history_today_follows_the_shanghai_digest_date(tmp_path, monkeypatch) -> None:
    _freeze_digest_clock(monkeypatch)

    def story(day: str) -> str:
        return (
            f"### [Atlas release](https://example.com/{day}) ⭐️ 8.0/10\n\n"
            "Atlas release notes.\n\nrss · Example · Nov 16, 10:00\n\n---\n\n"
        )

    (tmp_path / f"horizon-{UTC_TODAY}-en.md").write_text(story(UTC_TODAY), encoding="utf-8")
    (tmp_path / f"horizon-{SHANGHAI_TODAY}-en.md").write_text(story(SHANGHAI_TODAY), encoding="utf-8")

    results = asyncio.run(HistorySearchTool(tmp_path).execute({"query": "Atlas", "days": 7}))

    assert [entry["url"] for entry in results] == [f"https://example.com/{UTC_TODAY}"]

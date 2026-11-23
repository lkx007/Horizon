"""Historical digest dates cannot relabel a live fetch."""

import asyncio
from datetime import datetime, timezone
from pathlib import Path

import pytest

from src.digest_date import digest_date_str
from src.models import AIConfig, Config, SourcesConfig
from src.orchestrator import HorizonOrchestrator
from src.replay import ReplayRefusal, plan_digest_run, resolve_cli_action
from src.storage.manager import StorageManager
from tests.test_digest_date import (
    SHANGHAI_TODAY,
    _freeze_digest_clock,
    _item,
)


ROOT = Path(__file__).resolve().parents[1]


def test_schedule_ignores_a_requested_historical_date() -> None:
    plan = plan_digest_run(
        event="schedule",
        shanghai_today="2026-11-23",
        requested_date="2026-11-22",
        dry_run=True,
    )

    assert plan.mode == "scheduled-live"
    assert plan.digest_date == "2026-11-23"
    assert plan.run_live_horizon is True
    assert plan.publish is True
    assert plan.dry_run is False


def test_dispatch_of_yesterday_does_not_fetch_or_publish() -> None:
    plan = plan_digest_run(
        event="workflow_dispatch",
        shanghai_today="2026-11-23",
        requested_date="2026-11-22",
        dry_run=False,
    )

    assert plan.mode == "historical-preview"
    assert plan.digest_date == "2026-11-22"
    assert plan.run_live_horizon is False
    assert plan.publish is False
    assert plan.dry_run is True


def test_manual_today_still_publishes() -> None:
    plan = plan_digest_run(
        event="workflow_dispatch",
        shanghai_today="2026-11-23",
        requested_date="",
        dry_run=False,
    )

    assert plan.mode == "manual-live"
    assert plan.publish is True
    assert plan.run_live_horizon is True


def test_cli_refuses_to_publish_a_past_date() -> None:
    with pytest.raises(ReplayRefusal, match="Refusing to publish"):
        resolve_cli_action(
            requested_date="2026-11-22",
            dry_run=False,
            from_published=None,
            shanghai_today="2026-11-23",
        )


def test_cli_past_dry_run_requires_the_published_page() -> None:
    with pytest.raises(ReplayRefusal, match="does not fetch RSS"):
        resolve_cli_action(
            requested_date="2026-11-22",
            dry_run=True,
            from_published=None,
            shanghai_today="2026-11-23",
        )


def test_cli_past_dry_run_replays_the_published_page() -> None:
    assert (
        resolve_cli_action(
            requested_date="2026-11-22",
            dry_run=True,
            from_published="published.html",
            shanghai_today="2026-11-23",
        )
        == "published-replay"
    )


def test_workflow_keeps_the_schedule_and_blocks_historical_publish() -> None:
    text = (ROOT / ".github/workflows/daily-summary.yml").read_text(encoding="utf-8")

    assert "uv run horizon --hours 24" in text
    assert "steps.plan.outputs.publish == 'true'" in text
    assert "steps.plan.outputs.mode == 'historical-preview'" in text
    assert "render_ai_native_preview.py" in text
    assert "DASHSCOPE_API_KEY" in text
    assert text.index("uv run horizon --hours 24") < text.index("historical-preview")


def test_live_run_rejects_a_historical_digest_date_before_fetch(tmp_path, monkeypatch) -> None:
    _freeze_digest_clock(monkeypatch)
    orchestrator = HorizonOrchestrator(
        Config(
            ai=AIConfig(provider="openai", model="test", api_key_env="TEST_API_KEY"),
            sources=SourcesConfig(),
        ),
        StorageManager(str(tmp_path / "data")),
    )
    called = []

    async def fetch_all_sources(since):  # type: ignore[no-untyped-def]
        called.append(since)
        return []

    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)

    with pytest.raises(ReplayRefusal, match="Refusing to collect"):
        asyncio.run(orchestrator.run(digest_date="2026-11-22"))

    assert called == []
    assert digest_date_str() == SHANGHAI_TODAY


def test_dry_run_does_not_write_pages_or_notify(tmp_path, monkeypatch) -> None:
    _freeze_digest_clock(monkeypatch)
    orchestrator = HorizonOrchestrator(
        Config(
            ai=AIConfig(
                provider="openai",
                model="test",
                api_key_env="TEST_API_KEY",
                languages=["zh"],
            ),
            sources=SourcesConfig(),
        ),
        StorageManager(str(tmp_path / "data")),
    )
    notices = []

    class Notifier:
        async def send_failure(self, date: str, error_message: str) -> None:
            notices.append((date, error_message))

        async def send_daily_summary(self, **kwargs):  # type: ignore[no-untyped-def]
            notices.append(kwargs)

    orchestrator.webhook_notifier = Notifier()
    monkeypatch.chdir(tmp_path)

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
    monkeypatch.setattr(
        "src.orchestrator.DailySummarizer",
        __import__("tests.test_digest_date", fromlist=["_Summarizer"])._Summarizer,
    )

    asyncio.run(orchestrator.run(dry_run=True))

    assert not (tmp_path / "docs" / "_posts").exists()
    preview = tmp_path / "data" / "previews" / f"horizon-{SHANGHAI_TODAY}-zh.md"
    assert preview.exists()
    assert SHANGHAI_TODAY in preview.read_text(encoding="utf-8")
    assert notices == []


def test_replay_preview_keeps_published_november_22_counts(tmp_path) -> None:
    from scripts.render_ai_native_preview import build_preview_html, replay_note

    published = """<!DOCTYPE html><html><head>
<link rel="stylesheet" href="/Horizon/assets/css/style.css?v=abc">
<link rel="stylesheet" href="/Horizon/assets/css/horizon.css">
<script src="/Horizon/assets/js/horizon.js" defer></script>
</head><body><main>
<blockquote><p>从 26 条内容中筛选出 11 条重要资讯。</p></blockquote>
<hr />
<h2 id="科技新闻">科技新闻</h2>
<p>昨天的已发布条目</p>
<footer class="site-footer">footer</footer>
</main></body></html>
"""
    payload = {
        "digest_date": "2026-11-22",
        "sections": [
            {
                "id": "ai-native-product",
                "name": "AI-native product design",
                "display_names": {"zh": "AI Native 产品设计"},
            }
        ],
        "items": [
            {
                "section": "ai-native-product",
                "title": "围绕模型能力重做",
                "url": "https://hex.tech/blog/bitter-lessons-building-ai-in-hex-product-management/",
                "author": "Olivia Koshy",
                "feed_name": "Hex",
                "published_on": "2025-10-09",
                "tags": [],
                "blocks": {
                    "why_read": {"title": "为什么值得读", "content": "复盘。"},
                    "applicability": {"title": "适用条件", "content": "已有产品。"},
                    "how_to_try": {"title": "怎样试", "content": "对照三个问题。"},
                    "evidence": {"title": "结果与说法", "content": "10 倍是作者判断。"},
                },
            }
        ],
    }
    html = build_preview_html(
        published,
        payload,
        theme_css="/*theme*/",
        horizon_css="/*horizon*/",
        horizon_js="/*js*/",
        supplement_note=replay_note("2026-11-22"),
        banner_comment="<!-- Replay preview of the published 2026-11-22 page. Not a pipeline rerun. -->",
    )

    assert "从 26 条内容中筛选出 11 条重要资讯。" in html
    assert "昨天的已发布条目" in html
    assert "重放预览，不是重新采集" in html
    assert "Not a pipeline rerun" in html
    assert "https://hex.tech/blog/bitter-lessons-building-ai-in-hex-product-management/" in html
    assert "/10" not in html.split("AI Native", 1)[1]

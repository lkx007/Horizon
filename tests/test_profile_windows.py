"""AI-native uses a 7-day window; other profiles stay on 24 hours."""

from __future__ import annotations

import asyncio
from datetime import datetime, timedelta, timezone
from pathlib import Path

from src.ai.summarizer import DailySummarizer
from src.models import (
    AIConfig,
    ClassificationResult,
    CollectionConfig,
    ContentAnalysis,
    ContentItem,
    HackerNewsConfig,
    ProcessingConfig,
    ProcessingResult,
    ProfileSettingsConfig,
    RSSSourceConfig,
    RedditConfig,
    RedditSubredditConfig,
    SourcesConfig,
    SourceType,
    TelegramConfig,
)
from src.orchestrator import HorizonOrchestrator
from src.processing.profiles import ProfileRegistry
from src.processing.windows import (
    default_window_hours,
    fetch_hours_for_route,
    profile_window_hours,
    restrict_route,
)
from src.scrapers.base import FetchResult
from src.storage.manager import StorageManager

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime(2026, 11, 26, 1, 0, tzinfo=timezone.utc)
KNOWN = ("tech-news", "tech-blog", "finance-news", "ai-native")
SHORT = ("tech-news", "tech-blog", "finance-news")


def _settings() -> dict[str, ProfileSettingsConfig]:
    return {
        "tech-news": ProfileSettingsConfig(threshold=7.0),
        "tech-blog": ProfileSettingsConfig(threshold=4.0, topic_dedup=False),
        "finance-news": ProfileSettingsConfig(threshold=7.0),
        "ai-native": ProfileSettingsConfig(
            threshold=7.0, topic_dedup=False, time_window_hours=168
        ),
    }


def _window_for(profile_id: str) -> int:
    return profile_window_hours(profile_id, _settings(), 24)


def _item(
    title: str,
    *,
    age: timedelta,
    route: str | list[str],
    resolved: str | None = None,
) -> ContentItem:
    item = ContentItem(
        id=f"rss:{title}",
        source_type=SourceType.RSS,
        title=title,
        url=f"https://example.com/{title}",
        published_at=NOW - age,
        profile=route,
    )
    if resolved is not None:
        item.processing = ProcessingResult(
            classification=ClassificationResult(
                profile=resolved, method="source_override"
            ),
            analysis=ContentAnalysis(score=8.0, reason="test", summary=title),
        )
    return item


def test_actions_hours_flag_does_not_shrink_the_ai_native_window() -> None:
    # The daily workflow passes --hours 24. That replaces only the default.
    default = default_window_hours(24, 24)
    assert default == 24
    assert profile_window_hours("ai-native", _settings(), default) == 168
    for profile_id in SHORT:
        assert profile_window_hours(profile_id, _settings(), default) == 24


def test_source_fetch_uses_the_widest_routable_window() -> None:
    def hours(route):
        return fetch_hours_for_route(route, KNOWN, _window_for, 24)

    assert hours("tech-news") == 24
    assert hours("tech-blog") == 24
    assert hours("finance-news") == 24
    assert hours("ai-native") == 168
    assert hours(["tech-news", "ai-native"]) == 168
    assert hours(["tech-blog", "ai-native"]) == 168
    assert hours(None) == 168


def test_live_config_keeps_24h_profiles_and_extends_only_ai_native(monkeypatch) -> None:
    monkeypatch.setenv("LWN_KEY", "test")
    config = StorageManager(
        str(ROOT / "data"), str(ROOT / "data" / "config.github.json")
    ).load_config()
    settings = config.processing.profile_settings
    assert config.collection.time_window_hours == 24
    assert settings["ai-native"].time_window_hours == 168
    for profile_id in SHORT:
        assert settings[profile_id].time_window_hours is None

    def hours(route):
        return fetch_hours_for_route(
            route,
            KNOWN,
            lambda profile_id: profile_window_hours(profile_id, settings, 24),
            24,
        )

    by_name = {source.name: hours(source.profile) for source in config.sources.rss}
    assert by_name["Simon Willison"] == 24
    assert by_name["vLLM Blog"] == 24
    assert by_name["CNBC Finance"] == 24
    assert by_name["OpenAI News"] == 24
    assert by_name["Eugene Yan"] == 168
    assert by_name["LoopForge Blog"] == 168
    assert by_name["GitHub Trending - Daily"] == 168
    assert by_name["Meituan Tech"] == 168
    assert by_name["Google AI Blog"] == 168

    releases = {
        f"{source.owner}/{source.repo}": hours(source.profile)
        for source in config.sources.github
        if source.type == "repo_releases"
    }
    assert releases["NVIDIA/TensorRT-LLM"] == 24
    assert releases["anthropics/claude-code"] == 168
    assert releases["vllm-project/vllm"] == 24


def test_older_dual_profile_item_can_only_remain_ai_native() -> None:
    three_days = timedelta(hours=72)
    keep, route = restrict_route(
        ["tech-news", "ai-native"],
        NOW - three_days,
        now=NOW,
        known_ids=KNOWN,
        window_for=_window_for,
    )
    assert keep is True
    assert route == "ai-native"

    keep, route = restrict_route(
        ["tech-blog", "ai-native"],
        NOW - timedelta(hours=25),
        now=NOW,
        known_ids=KNOWN,
        window_for=_window_for,
    )
    assert keep is True
    assert route == "ai-native"

    recent = ["tech-news", "ai-native"]
    keep, route = restrict_route(
        recent,
        NOW - timedelta(hours=3),
        now=NOW,
        known_ids=KNOWN,
        window_for=_window_for,
    )
    assert keep is True
    assert route is recent


def test_25_to_168_hour_items_stay_out_of_short_profiles() -> None:
    for profile_id in SHORT:
        for age in (timedelta(hours=25), timedelta(hours=72), timedelta(hours=168)):
            keep, _route = restrict_route(
                profile_id,
                NOW - age,
                now=NOW,
                known_ids=KNOWN,
                window_for=_window_for,
            )
            assert keep is False

    keep, route = restrict_route(
        "ai-native",
        NOW - timedelta(hours=168),
        now=NOW,
        known_ids=KNOWN,
        window_for=_window_for,
    )
    assert keep is True
    assert route == "ai-native"

    keep, _route = restrict_route(
        "ai-native",
        NOW - timedelta(hours=168, seconds=1),
        now=NOW,
        known_ids=KNOWN,
        window_for=_window_for,
    )
    assert keep is False


def test_orchestrator_selects_old_items_only_for_ai_native() -> None:
    registry = ProfileRegistry.load(ROOT / "profiles", "tech-news")
    orchestrator = HorizonOrchestrator.__new__(HorizonOrchestrator)
    orchestrator.config = type("Cfg", (), {})()
    orchestrator.config.processing = ProcessingConfig(profile_settings=_settings())
    orchestrator.profiles = registry

    trending = _item(
        "trending-repo", age=timedelta(hours=72), route=["tech-news", "ai-native"]
    )
    native = _item("practice-note", age=timedelta(hours=168), route="ai-native")
    fresh_news = _item("fresh-news", age=timedelta(hours=2), route="tech-news")
    stale_news = _item("stale-news", age=timedelta(hours=25), route="tech-news")
    stale_blog = _item("stale-blog", age=timedelta(hours=30), route="tech-blog")
    stale_finance = _item("stale-finance", age=timedelta(hours=48), route="finance-news")
    fresh_dual = _item(
        "fresh-dual", age=timedelta(hours=1), route=["tech-blog", "ai-native"]
    )

    kept = orchestrator.restrict_to_profile_windows(
        [trending, native, fresh_news, stale_news, stale_blog, stale_finance, fresh_dual],
        24,
        NOW,
    )

    assert [item.title for item in kept] == [
        "trending-repo",
        "practice-note",
        "fresh-news",
        "fresh-dual",
    ]
    assert trending.profile == "ai-native"
    assert native.profile == "ai-native"
    assert fresh_news.profile == "tech-news"
    assert fresh_dual.profile == ["tech-blog", "ai-native"]

    trending.processing = ProcessingResult(
        classification=ClassificationResult(profile="ai-native", method="source_override"),
        analysis=ContentAnalysis(score=8.0, reason="test", summary="trending"),
    )
    native.processing = ProcessingResult(
        classification=ClassificationResult(profile="ai-native", method="source_override"),
        analysis=ContentAnalysis(score=8.0, reason="test", summary="native"),
    )
    fresh_news.processing = ProcessingResult(
        classification=ClassificationResult(profile="tech-news", method="source_override"),
        analysis=ContentAnalysis(score=8.0, reason="test", summary="news"),
    )
    leaked = _item(
        "leaked-news",
        age=timedelta(hours=72),
        route="ai-native",
        resolved="tech-news",
    )
    selected = orchestrator.drop_outside_resolved_window(
        [trending, native, fresh_news, leaked], 24, NOW
    )
    assert [item.title for item in selected] == [
        "trending-repo",
        "practice-note",
        "fresh-news",
    ]

    view = DailySummarizer(
        profile_names=registry.names,
        profile_order=["tech-news", "tech-blog", "finance-news", "ai-native"],
    ).build_view(selected, "zh")
    groups = {group.profile_id: [item.item.title for item in group.items] for group in view.groups}
    assert groups["tech-news"] == ["fresh-news"]
    assert "trending-repo" not in groups["tech-news"]
    assert "practice-note" not in groups["tech-news"]
    assert set(groups["ai-native"]) == {"trending-repo", "practice-note"}
    assert "tech-blog" not in groups
    assert "finance-news" not in groups


def test_fetch_splits_24h_sources_from_ai_native_sources(monkeypatch) -> None:
    recorded: list[tuple[str, tuple[str, ...], datetime]] = []

    class RecordingRSS:
        def __init__(self, sources, client, extractors=None):
            self.sources = sources

        async def fetch(self, since):  # type: ignore[no-untyped-def]
            recorded.append(
                ("rss", tuple(source.name for source in self.sources), since)
            )
            return FetchResult()

    class RecordingReddit:
        def __init__(self, config, client):
            self.config = config

        async def fetch(self, since):  # type: ignore[no-untyped-def]
            recorded.append(
                (
                    "reddit",
                    tuple(sub.subreddit for sub in self.config.subreddits),
                    since,
                )
            )
            return FetchResult()

    monkeypatch.setattr("src.orchestrator.RSSScraper", RecordingRSS)
    monkeypatch.setattr("src.orchestrator.RedditScraper", RecordingReddit)
    registry = ProfileRegistry.load(ROOT / "profiles", "tech-news")
    orchestrator = HorizonOrchestrator(
        _config(),
        StorageManager(str(ROOT / "data"), str(ROOT / "data" / "config.github.json")),
        profiles=registry,
    )
    since = NOW - timedelta(hours=24)

    asyncio.run(
        orchestrator.fetch_all_sources(since, default_window_hours=24, now=NOW)
    )

    rss = {names: cutoff for kind, names, cutoff in recorded if kind == "rss"}
    assert rss[("News", "Blog", "Finance")] == since
    assert rss[("Native", "Trending")] == NOW - timedelta(hours=168)
    reddit = {names: cutoff for kind, names, cutoff in recorded if kind == "reddit"}
    assert reddit[("MachineLearning",)] == since
    assert reddit[("AINative",)] == NOW - timedelta(hours=168)


def _config():
    from src.models import Config

    return Config(
        ai=AIConfig(provider="openai", model="test", api_key_env="TEST_API_KEY"),
        processing=ProcessingConfig(
            profiles_dir=str(ROOT / "profiles"),
            profile_settings=_settings(),
        ),
        collection=CollectionConfig(time_window_hours=24),
        sources=SourcesConfig(
            hackernews=HackerNewsConfig(enabled=False),
            telegram=TelegramConfig(enabled=False),
            reddit=RedditConfig(
                subreddits=[
                    RedditSubredditConfig(
                        subreddit="MachineLearning", profile="tech-news"
                    ),
                    RedditSubredditConfig(subreddit="AINative", profile="ai-native"),
                ]
            ),
            rss=[
                RSSSourceConfig(
                    name="News", url="https://example.com/news.xml", profile="tech-news"
                ),
                RSSSourceConfig(
                    name="Blog", url="https://example.com/blog.xml", profile="tech-blog"
                ),
                RSSSourceConfig(
                    name="Finance",
                    url="https://example.com/finance.xml",
                    profile="finance-news",
                ),
                RSSSourceConfig(
                    name="Native",
                    url="https://example.com/native.xml",
                    profile="ai-native",
                ),
                RSSSourceConfig(
                    name="Trending",
                    url="https://example.com/trending.xml",
                    profile=["tech-news", "ai-native"],
                ),
            ],
        ),
    )

"""AI-native profile, digest subsections, and the preserved daily runtime."""

import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

import pytest
from pydantic import ValidationError

from src.ai.summarizer import DailySummarizer
from src.models import (
    AIConfig,
    Config,
    ContentAnalysis,
    ContentArtifact,
    ContentBlock,
    ContentItem,
    DigestConfig,
    ProcessingResult,
    ClassificationResult,
    SourcesConfig,
    SourceType,
    TopicSectionConfig,
)
from src.orchestrator import HorizonOrchestrator
from src.processing.profiles import ProfileRegistry
from src.storage.manager import StorageManager

ROOT = Path(__file__).resolve().parents[1]

SECTIONS = [
    TopicSectionConfig(
        id="ai-native-product",
        name="AI-native product design",
        display_names={"zh": "AI Native 产品设计"},
    ),
    TopicSectionConfig(
        id="ai-native-workflow",
        name="Team workflows",
        display_names={"zh": "团队工作流与人机协作"},
    ),
    TopicSectionConfig(
        id="ai-native-cases",
        name="Implementation cases",
        display_names={"zh": "落地案例、方法与失败教训"},
    ),
]


def _run(coro):
    return asyncio.run(coro)


def _item(
    idx: int,
    *,
    profile: str = "ai-native",
    title: str = "",
    category: str | None = None,
    tags: list[str] | None = None,
    unscored: bool = False,
) -> ContentItem:
    item = ContentItem(
        id=f"rss:item-{idx}",
        source_type=SourceType.RSS,
        title=title or f"Item {idx}",
        url=f"https://example.com/items/{idx}",
        author="author",
        published_at=datetime(2025, 10, 9, tzinfo=timezone.utc),
        profile=profile,
        metadata={"feed_name": "Example", "category": category},
        processing=ProcessingResult(
            classification=ClassificationResult(
                profile=profile, method="source_override"
            ),
            analysis=ContentAnalysis(
                score=None if unscored else 8.0,
                reason="test",
                summary="One sentence.",
                tags=tags or [],
            ),
            artifacts={
                "zh": ContentArtifact(
                    language="zh",
                    title=title or f"Item {idx}",
                    blocks=[
                        ContentBlock(
                            id="why_read",
                            title="为什么值得读",
                            content="Worth reading.",
                            primary=True,
                        )
                    ],
                )
            },
        ),
    )
    if unscored:
        item.metadata["unscored"] = True
    return item


def test_ai_native_profile_loads_and_states_the_editorial_bar():
    registry = ProfileRegistry.load(ROOT / "profiles", "tech-news")
    profile = registry.get("ai-native")

    assert profile.definition.display_names["zh"] == "AI Native 实践"
    block_ids = [block.id for block in profile.definition.enrichment.blocks]
    assert block_ids == ["why_read", "applicability", "how_to_try", "evidence"]
    assert profile.definition.enrichment.blocks[0].primary is True
    combined = "\n".join(
        [profile.match_prompt, profile.analysis_prompt, profile.enrichment_prompt]
    )
    for section_id in (
        "ai-native-product",
        "ai-native-workflow",
        "ai-native-cases",
    ):
        assert section_id in combined
    assert "beginner" in profile.analysis_prompt.lower() or "API" in profile.match_prompt
    assert "marketing" in profile.match_prompt.lower()
    assert "sourced" in profile.enrichment_prompt.lower() or "测量" in profile.enrichment_prompt


def test_github_runtime_keeps_schedule_model_and_adds_ai_native(monkeypatch):
    monkeypatch.setenv("LWN_KEY", "test")
    config = StorageManager(str(ROOT / "data"), str(ROOT / "data" / "config.github.json")).load_config()

    assert config.ai.provider.value == "ali"
    assert config.ai.model == "qwen-plus"
    assert str(config.ai.base_url).rstrip("/") == "https://dashscope.aliyuncs.com/compatible-mode/v1"
    assert config.ai.api_key_env == "DASHSCOPE_API_KEY"
    assert config.ai.languages == ["zh", "en"]
    assert config.webhook is not None and config.webhook.enabled is False
    assert config.email is None
    assert config.processing.profile_settings["ai-native"].threshold == 7.0
    assert config.processing.profile_settings["ai-native"].topic_dedup is False
    assert config.digest.profile_order == [
        "tech-news",
        "tech-blog",
        "finance-news",
        "ai-native",
    ]
    assert [section.id for section in config.digest.topic_sections["ai-native"]] == [
        "ai-native-product",
        "ai-native-workflow",
        "ai-native-cases",
    ]
    feed_names = [source.name for source in config.sources.rss]
    for name in (
        "Simon Willison",
        "vLLM Blog",
        "Sean Goedecke",
        "CNBC Finance",
        "LWN.net",
        "Eugene Yan",
        "Hamel Husain",
        "Zalando Engineering",
        "Chip Huyen",
    ):
        assert name in feed_names
    assert "https://philcalcado.com/feed.xml" in [str(source.url) for source in config.sources.rss]

    workflow = (ROOT / ".github" / "workflows" / "daily-summary.yml").read_text(
        encoding="utf-8"
    )
    assert 'timezone: "Asia/Shanghai"' in workflow
    for cron in ("'17 0 * * *'", "'52 8 * * *'", "'17 12 * * *'", "'23 15 * * *'"):
        assert cron in workflow
    assert "DASHSCOPE_API_KEY" in workflow
    assert "publish_branch: gh-pages" in workflow
    assert "smtp" not in workflow.lower()


_BLOG = ["tech-blog", "ai-native"]
_NEWS = ["tech-news", "ai-native"]


def test_github_runtime_routes_trending_and_core_official_sources(monkeypatch):
    monkeypatch.setenv("LWN_KEY", "test")
    config = StorageManager(
        str(ROOT / "data"), str(ROOT / "data" / "config.github.json")
    ).load_config()
    registry = ProfileRegistry.load(ROOT / "profiles", config.processing.default_profile)
    registry.validate_source_references(config.sources.model_dump(mode="json"))

    assert config.collection.time_window_hours == 24
    assert config.sources.ossinsight.enabled is False

    feeds = [
        (source.name, str(source.url), source.profile, source.content_extractor)
        for source in config.sources.rss
    ]
    assert feeds == [
        ("Simon Willison", "https://simonwillison.net/atom/everything/", "tech-news", None),
        ("vLLM Blog", "https://vllm.ai/blog/rss.xml", "tech-blog", "trafilatura"),
        ("Sean Goedecke", "https://www.seangoedecke.com/rss.xml", "tech-blog", "trafilatura"),
        (
            "CNBC Finance",
            "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000664",
            "finance-news",
            "trafilatura",
        ),
        (
            "GitHub Trending - Daily",
            "https://mshibanami.github.io/GitHubTrendingRSS/daily/all.xml",
            _NEWS,
            None,
        ),
        ("Semianalysis", "https://newsletter.semianalysis.com/feed", "tech-news", None),
        ("LWN.net", "https://lwn.net/headlines/full_text?key=test", "tech-news", None),
        ("Eugene Yan", "https://eugeneyan.com/rss/", "ai-native", "trafilatura"),
        ("Hamel Husain", "https://hamel.dev/index.xml", "ai-native", "trafilatura"),
        ("Phil Calçado", "https://philcalcado.com/feed.xml", "ai-native", "trafilatura"),
        ("Zalando Engineering", "https://engineering.zalando.com/atom.xml", "ai-native", "trafilatura"),
        ("Chip Huyen", "https://huyenchip.com/feed.xml", "ai-native", "trafilatura"),
        ("LoopForge Blog", "https://loopforge.cn/blog/feed.xml", "ai-native", "trafilatura"),
        ("Meituan Tech", "https://tech.meituan.com/atom.xml", _BLOG, "trafilatura"),
        ("QwenLM Blog", "https://qwenlm.github.io/blog/index.xml", _BLOG, "trafilatura"),
        ("Google DeepMind Blog", "https://deepmind.google/blog/rss.xml", _BLOG, "trafilatura"),
        ("Google Research Blog", "https://research.google/blog/rss/", _BLOG, "trafilatura"),
        (
            "Google AI Blog",
            "https://blog.google/innovation-and-ai/technology/ai/rss/",
            _NEWS,
            "trafilatura",
        ),
        ("Engineering at Meta", "https://engineering.fb.com/feed/", _BLOG, "trafilatura"),
        ("Microsoft Research", "https://www.microsoft.com/en-us/research/feed/", _BLOG, "trafilatura"),
        ("GitHub Engineering", "https://github.blog/engineering/feed/", _BLOG, "trafilatura"),
        ("GitHub AI and ML", "https://github.blog/ai-and-ml/feed/", _NEWS, "trafilatura"),
        ("AWS Architecture Blog", "https://aws.amazon.com/blogs/architecture/feed/", _BLOG, "trafilatura"),
        ("Amazon Science", "https://www.amazon.science/index.rss", _BLOG, "trafilatura"),
        ("Apple Machine Learning", "https://machinelearning.apple.com/rss.xml", _BLOG, "trafilatura"),
        ("OpenAI News", "https://openai.com/news/rss.xml", "tech-news", "trafilatura"),
        ("Mistral AI News", "https://mistral.ai/news/rss", _NEWS, "trafilatura"),
        ("NVIDIA Technical Blog", "https://developer.nvidia.com/blog/feed", _BLOG, "trafilatura"),
        ("Cloudflare Blog", "https://blog.cloudflare.com/rss/", _BLOG, "trafilatura"),
        ("Netflix TechBlog", "https://netflixtechblog.com/feed", _BLOG, "trafilatura"),
        ("Airbnb Engineering", "https://airbnb.tech/feed/", _BLOG, "trafilatura"),
        ("Stripe Blog", "https://stripe.com/blog/feed.rss", _NEWS, "trafilatura"),
        ("Stripe Developer Blog", "https://stripe.dev/blog/feed", _BLOG, "trafilatura"),
        ("Shopify Engineering", "https://shopify.engineering/blog.atom", _BLOG, "trafilatura"),
        ("Spotify Engineering", "https://engineering.atspotify.com/feed", _BLOG, "trafilatura"),
        ("Hugging Face Blog", "https://huggingface.co/blog/feed.xml", _BLOG, "trafilatura"),
        ("Together AI Blog", "https://www.together.ai/blog/rss.xml", _BLOG, "trafilatura"),
        ("Pinterest Engineering", "https://medium.com/feed/pinterest-engineering", _BLOG, "trafilatura"),
        ("Lyft Engineering", "https://eng.lyft.com/feed", _BLOG, "trafilatura"),
        ("Dropbox Tech", "https://dropbox.tech/feed", _BLOG, "trafilatura"),
        ("Salesforce Engineering", "https://engineering.salesforce.com/feed/", _BLOG, "trafilatura"),
        ("Atlassian How We Build", "https://www.atlassian.com/blog/how-we-build/feed", _BLOG, "trafilatura"),
    ]
    trending_urls = [url for _, url, _, _ in feeds if "GitHubTrendingRSS" in url]
    assert trending_urls == [
        "https://mshibanami.github.io/GitHubTrendingRSS/daily/all.xml"
    ]

    releases = [
        (source.type, source.owner, source.repo, source.profile)
        for source in config.sources.github
        if source.type == "repo_releases"
    ]
    assert releases == [
        ("repo_releases", "vllm-project", "vllm", "tech-news"),
        ("repo_releases", "sgl-project", "sglang", "tech-news"),
        ("repo_releases", "triton-lang", "triton", "tech-news"),
        ("repo_releases", "Tencent", "LoopForge", _NEWS),
        ("repo_releases", "Tencent", "WeKnora", _NEWS),
        ("repo_releases", "Tencent", "BrowserSkill", _NEWS),
        ("repo_releases", "QwenLM", "qwen-code", _NEWS),
        ("repo_releases", "agentscope-ai", "agentscope", _NEWS),
        ("repo_releases", "anthropics", "claude-code", _NEWS),
        ("repo_releases", "google-gemini", "gemini-cli", _NEWS),
        ("repo_releases", "ml-explore", "mlx", _NEWS),
        ("repo_releases", "NVIDIA", "TensorRT-LLM", "tech-news"),
    ]


def test_topic_sections_group_without_disturbing_news_items():
    news = _item(1, profile="tech-news", title="Frontier item", tags=["models"])
    news.processing.artifacts["zh"].blocks[0].content = "News body."
    product = _item(
        2,
        title="Product piece",
        category="ai-native-product",
        tags=["ai-native-workflow"],
    )
    workflow = _item(3, title="Workflow piece", tags=["ai-native-workflow"])
    case = _item(4, title="Case piece", tags=["AI Native Cases"])
    summarizer = DailySummarizer(
        profile_names={
            "tech-news": {"zh": "科技新闻"},
            "ai-native": {"zh": "AI Native 实践"},
        },
        profile_order=["tech-news", "ai-native"],
        topic_sections={"ai-native": SECTIONS},
    )

    result = _run(
        summarizer.generate_summary(
            [case, product, news, workflow],
            date="2026-11-23",
            total_fetched=27,
            language="zh",
        )
    )

    body = result.split("\n\n---\n\n", 2)[2]
    assert body.index("## 科技新闻") < body.index("## AI Native 实践")
    assert "### [Frontier item]" in body
    assert body.index("### AI Native 产品设计") < body.index("Product piece")
    assert body.index("Product piece") < body.index("### 团队工作流与人机协作")
    assert body.index("### 团队工作流与人机协作") < body.index("Workflow piece")
    assert body.index("Workflow piece") < body.index("### 落地案例、方法与失败教训")
    assert "#### [Case piece]" in body


def test_unscored_supplement_omits_score_and_empty_sections():
    item = _item(1, title="Supplemental", tags=["ai-native-product"], unscored=True)
    summarizer = DailySummarizer(
        profile_names={"ai-native": {"zh": "AI Native 实践"}},
        topic_sections={"ai-native": SECTIONS},
    )

    result = _run(
        summarizer.generate_summary([item], "2026-11-23", 27, language="zh")
    )

    assert "Supplemental" in result
    assert "/10" not in result
    assert "团队工作流" not in result
    assert "落地案例" not in result
    assert "其他" not in result


def test_unmatched_ai_native_item_lands_in_other():
    item = _item(1, title="Untagged", tags=["evals"])
    summarizer = DailySummarizer(
        profile_names={"ai-native": {"en": "AI-native practice"}},
        topic_sections={"ai-native": SECTIONS},
    )

    result = _run(
        summarizer.generate_summary([item], "2026-11-23", 4, language="en")
    )

    assert "### Other" in result
    assert "#### [Untagged]" in result


def test_rejects_unknown_topic_section_profile():
    config = Config(
        ai=AIConfig(provider="openai", model="test", api_key_env="TEST_API_KEY"),
        sources=SourcesConfig(),
        digest=DigestConfig(
            topic_sections={"missing": [TopicSectionConfig(id="ai-native-product", name="Product")]}
        ),
    )

    with pytest.raises(ValueError, match="topic_sections contains unknown profiles"):
        HorizonOrchestrator(config, object())


def test_rejects_duplicate_topic_section_ids():
    with pytest.raises(ValidationError):
        DigestConfig(
            topic_sections={
                "ai-native": [
                    TopicSectionConfig(id="ai-native-product", name="One"),
                    TopicSectionConfig(id="ai-native-product", name="Two"),
                ]
            }
        )


def test_preview_sources_render_three_real_articles():
    from scripts.render_ai_native_preview import markdown_fragment, render_section_markdown

    payload = json.loads(
        (ROOT / "previews" / "2026-11-23-ai-native-sources.json").read_text(encoding="utf-8")
    )
    toc, body = render_section_markdown(payload)
    toc_html = markdown_fragment(toc)

    assert toc_html.count("<li>") == 3
    assert "### AI Native 产品设计" in body
    assert "### 团队工作流与人机协作" in body
    assert "### 落地案例、方法与失败教训" in body
    assert "https://hex.tech/blog/bitter-lessons-building-ai-in-hex-product-management/" in body
    assert "https://sketch.dev/blog/our-first-outage-from-llm-written-code" in body
    assert "dead-ends-or-data-goldmines-ai-powered-postmortem-analysis.html" in body
    assert "/10" not in body
    assert "2025-10-09" in body
    assert "2025-07-31" in body
    assert "2025-09-25" in body


def test_preview_splice_keeps_original_digest_and_embeds_assets():
    from scripts.render_ai_native_preview import splice_preview

    live = """<!DOCTYPE html>
<html><head>
<link rel="stylesheet" href="/Horizon/assets/css/style.css?v=abc">
<link rel="stylesheet" href="/Horizon/assets/css/horizon.css">
<script src="/Horizon/assets/js/horizon.js" defer></script>
</head><body>
<main id="content" class="main-content">
<blockquote><p>从 27 条内容中筛选出 13 条重要资讯。</p></blockquote>
<hr />
<p><strong>科技新闻</strong></p>
<hr />
<h2 id="科技新闻">科技新闻</h2>
<p>硅谷重心从信息导航转向 AI 驱动增长</p>
<footer class="site-footer">footer</footer>
</main></body></html>
"""
    rendered = splice_preview(
        live,
        toc_html="<p><strong>AI Native 实践</strong></p>",
        section_html="<h2>AI Native 实践</h2><p>补充阅读</p>",
        theme_css="/*theme*/",
        horizon_css="/*horizon*/",
        horizon_js="/*js*/",
    )

    assert "从 27 条内容中筛选出 13 条重要资讯。" in rendered
    assert "硅谷重心从信息导航转向 AI 驱动增长" in rendered
    assert "<h2>AI Native 实践</h2>" in rendered
    assert 'href="/Horizon/assets/css/style.css' not in rendered
    assert 'src="/Horizon/assets/js/horizon.js"' not in rendered
    assert "/*theme*/" in rendered
    assert "/*horizon*/" in rendered
    assert "/*js*/" in rendered
    assert rendered.index("AI Native 实践") < rendered.index("硅谷重心")
    assert rendered.index("<h2>AI Native 实践</h2>") > rendered.index("科技新闻</h2>")

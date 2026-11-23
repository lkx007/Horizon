"""Render a standalone preview of a published Horizon page plus an AI-native section.

The section is assembled from already retrieved public sources. This script does
not call a model, send mail, or write to docs/ or gh-pages.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import markdown

from src.ai.summarizer import DailySummarizer
from src.models import (
    ArtifactSource,
    ClassificationResult,
    ContentAnalysis,
    ContentArtifact,
    ContentBlock,
    ContentItem,
    ProcessingResult,
    SourceType,
    TopicSectionConfig,
)

NEWS_HEADING = '<h2 id="科技新闻">'
FOOTER = '<footer class="site-footer">'
SUPPLEMENT_NOTE = (
    "补充阅读，不是 2026-11-23 当天抓取的新闻。下面三篇来自公开原文，"
    "发布日期写在来源行，以各页面标明的日期为准。本栏没有调用 DashScope，"
    "也没有编造评分。数字只转述原文里的测量或作者自己的观察，并分开写作者判断。"
)


def splice_preview(
    live_html: str,
    *,
    toc_html: str,
    section_html: str,
    theme_css: str,
    horizon_css: str,
    horizon_js: str,
) -> str:
    """Insert a section into a saved Pages HTML file and inline its assets."""
    if NEWS_HEADING not in live_html or FOOTER not in live_html:
        raise ValueError("live digest is missing the news heading or footer")
    heading_at = live_html.index(NEWS_HEADING)
    divider_at = live_html.rfind("<hr", 0, heading_at)
    if divider_at < 0:
        raise ValueError("live digest is missing the table-of-contents divider")

    rendered = live_html[:divider_at] + toc_html.strip() + "\n\n" + live_html[divider_at:]
    footer_at = rendered.index(FOOTER)
    rendered = rendered[:footer_at] + section_html.strip() + "\n\n" + rendered[footer_at:]
    rendered = re.sub(
        r'\s*<link rel="stylesheet" href="/Horizon/assets/css/style\.css[^"]*">',
        "\n<style>\n" + theme_css + "\n</style>",
        rendered,
        count=1,
    )
    rendered = re.sub(
        r'\s*<link rel="stylesheet" href="/Horizon/assets/css/horizon\.css">',
        "\n<style>\n" + horizon_css + "\n</style>",
        rendered,
        count=1,
    )
    rendered = rendered.replace(
        '<script src="/Horizon/assets/js/horizon.js" defer></script>',
        "<script>\n" + horizon_js + "\n</script>",
    )
    extra_css = (
        "<style>\n"
        ".ai-native-supplement{border-left:3px solid var(--hz-accent);"
        "background:var(--hz-surface);padding:0.7em 1em;color:var(--hz-text);}\n"
        "</style>\n"
    )
    rendered = rendered.replace("</head>", extra_css + "</head>", 1)
    if not rendered.startswith("<!--"):
        rendered = (
            "<!-- Local Horizon preview. Does not publish to gh-pages. "
            "The AI Native items are supplemental reading, not 2026-11-23 news. -->\n"
            + rendered
        )
    return rendered


def _sections_from_config(raw_sections: list[dict]) -> list[TopicSectionConfig]:
    return [TopicSectionConfig.model_validate(section) for section in raw_sections]


def _clock_label(published_on: str) -> str:
    parsed = datetime.fromisoformat(published_on)
    return f"{parsed.month}月{parsed.day}日 00:00"


def build_items(payload: dict) -> list[ContentItem]:
    items = []
    for index, raw in enumerate(payload["items"], start=1):
        published = datetime.fromisoformat(raw["published_on"]).replace(tzinfo=timezone.utc)
        blocks = [
            ContentBlock(
                id=block_id,
                title=raw["blocks"][block_id]["title"],
                content=raw["blocks"][block_id]["content"],
                primary=block_id == "why_read",
            )
            for block_id in ("why_read", "applicability", "how_to_try", "evidence")
        ]
        items.append(
            ContentItem(
                id=f"rss:ai-native:{index}",
                source_type=SourceType.RSS,
                title=raw["title"],
                url=raw["url"],
                author=raw["author"],
                published_at=published,
                profile="ai-native",
                metadata={
                    "feed_name": raw["feed_name"],
                    "category": raw["section"],
                    "unscored": True,
                },
                processing=ProcessingResult(
                    classification=ClassificationResult(
                        profile="ai-native", method="source_override"
                    ),
                    analysis=ContentAnalysis(
                        score=None,
                        reason="Supplemental reading assembled from the public source. Not scored by the daily model.",
                        summary=raw["blocks"]["why_read"]["content"],
                        tags=[raw["section"], *raw.get("tags", [])],
                    ),
                    artifacts={
                        "zh": ContentArtifact(
                            language="zh",
                            title=raw["title"],
                            blocks=blocks,
                            sources=[
                                ArtifactSource(
                                    id="original",
                                    title=f"原文，页面日期 {raw['published_on']}",
                                    url=raw["url"],
                                )
                            ],
                        )
                    },
                ),
            )
        )
    return items


def render_section_markdown(payload: dict) -> tuple[str, str]:
    items = build_items(payload)
    summarizer = DailySummarizer(
        profile_names={"ai-native": {"zh": "AI Native 实践"}},
        profile_order=["ai-native"],
        topic_sections={"ai-native": _sections_from_config(payload["sections"])},
    )
    summary = asyncio.run(
        summarizer.generate_summary(
            items,
            date=payload["digest_date"],
            total_fetched=payload.get("total_fetched", len(items)),
            language="zh",
        )
    )
    for raw in payload["items"]:
        summary = summary.replace(_clock_label(raw["published_on"]), raw["published_on"])
    header, toc, body = summary.split("\n\n---\n\n", 2)
    if not header.startswith("# "):
        raise ValueError("generated summary is missing the digest header")
    return toc.strip(), body.strip()


def markdown_fragment(source: str) -> str:
    # Python-Markdown keeps a following list inside the paragraph unless a
    # blank line separates them. Kramdown, which renders the live Pages, does
    # not. Insert that blank line so the preview TOC matches the live lists.
    source = re.sub(r"\n(\d+\. )", r"\n\n\1", source)
    return markdown.markdown(source, extensions=["extra", "sane_lists"])


def build_preview_html(
    live_html: str,
    payload: dict,
    *,
    theme_css: str,
    horizon_css: str,
    horizon_js: str,
) -> str:
    toc_md, body_md = render_section_markdown(payload)
    note = f"\n\n> {SUPPLEMENT_NOTE}\n"
    heading, rest = body_md.split("\n\n", 1)
    body_md = f"{heading}{note}\n{rest}"
    section_html = markdown_fragment(body_md).replace(
        "<blockquote>",
        '<blockquote class="ai-native-supplement">',
        1,
    )
    return splice_preview(
        live_html,
        toc_html=markdown_fragment(toc_md),
        section_html=section_html,
        theme_css=theme_css,
        horizon_css=horizon_css,
        horizon_js=horizon_js,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live-html", type=Path, required=True)
    parser.add_argument("--sources", type=Path, required=True)
    parser.add_argument("--theme-css", type=Path, required=True)
    parser.add_argument("--horizon-css", type=Path, required=True)
    parser.add_argument("--horizon-js", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    payload = json.loads(args.sources.read_text(encoding="utf-8"))
    html = build_preview_html(
        args.live_html.read_text(encoding="utf-8"),
        payload,
        theme_css=args.theme_css.read_text(encoding="utf-8"),
        horizon_css=args.horizon_css.read_text(encoding="utf-8"),
        horizon_js=args.horizon_js.read_text(encoding="utf-8"),
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(html, encoding="utf-8")
    print(args.out)


if __name__ == "__main__":
    main()

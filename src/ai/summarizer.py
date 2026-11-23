"""Daily summary generation — pure programmatic rendering."""

import html
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from urllib.parse import quote, urlsplit

from .localization import normalize_language
from ..models import ContentItem


_CJK = r"[\u4e00-\u9fff\u3400-\u4dbf]"
_ASCII = r"[A-Za-z0-9]"
_MARKDOWN_SPECIAL = re.compile(r"([\\`*_{}\[\]()<>#!|])")
_MARKDOWN_BLOCK_START = re.compile(r"(?m)^( {0,3})(>|[-+] |\d+[.)] )")
_URL_SAFE_CHARS = ":/?#[]@!$&'*,;=~%+"


def _escape_markdown(value: object) -> str:
    """Render untrusted text literally while retaining its readable content."""
    escaped = html.escape(str(value), quote=True)
    escaped = _MARKDOWN_SPECIAL.sub(r"\\\1", escaped)
    return _MARKDOWN_BLOCK_START.sub(r"\1\\\2", escaped)


def _safe_url(value: object) -> Optional[str]:
    """Return an HTML/Markdown-safe HTTP(S) URL, or None for unsafe URLs."""
    raw = str(value).strip()
    if not raw or any(ord(char) < 32 or ord(char) == 127 for char in raw):
        return None
    try:
        parsed = urlsplit(raw)
        if parsed.scheme.lower() not in {"http", "https"} or not parsed.netloc:
            return None
        parsed.port
    except (TypeError, ValueError):
        return None
    encoded = quote(raw, safe=_URL_SAFE_CHARS)
    return html.escape(encoded, quote=True)


def _pangu(text: str) -> str:
    """Insert a space between CJK and ASCII letters/digits (Pangu spacing)."""
    text = re.sub(rf"({_CJK})({_ASCII})", r"\1 \2", text)
    text = re.sub(rf"({_ASCII})({_CJK})", r"\1 \2", text)
    return text


LABELS = {
    "en": {
        "header": "Horizon Daily",
        "source": "Source",
        "background": "Background",
        "discussion": "Discussion",
        "references": "References",
        "tags": "Tags",
        "other_section": "Other",
        "selected_items": "From {total} items, {selected} important content pieces were selected",
        "empty_analyzed": "Analyzed {total} items, but none met the importance threshold.",
        "empty_body": (
            "No significant developments today. This might indicate:\n"
            "- A quiet day in your tracked sources\n"
            "- The AI score threshold is too high\n"
            "- Your information sources need expansion\n\n"
            "Consider:\n"
            "1. Lowering the configured profile threshold\n"
            "2. Adding more diverse information sources\n"
            "3. Checking if the AI model is working correctly\n"
        ),
    },
    "zh": {
        "header": "Horizon 每日速递",
        "source": "来源",
        "background": "背景",
        "discussion": "社区讨论",
        "references": "参考链接",
        "tags": "标签",
        "other_section": "其他",
        "selected_items": "从 {total} 条内容中筛选出 {selected} 条重要资讯。",
        "empty_analyzed": "已分析 {total} 条内容，但没有达到重要性阈值的条目。",
        "empty_body": (
            "今日暂无重要动态，可能原因：\n"
            "- 今天关注的信息源较平静\n"
            "- AI 评分阈值设置过高\n"
            "- 信息源种类有待扩充\n\n"
            "建议：\n"
            "1. 降低当前 Profile 的过滤阈值\n"
            "2. 添加更多多样化的信息源\n"
            "3. 检查 AI 模型是否正常工作\n"
        ),
    },
}


@dataclass(frozen=True)
class SummaryItemView:
    item: ContentItem
    index: int
    global_index: int
    group_count: int
    title: str
    score: float | str
    anchor_id: str


@dataclass(frozen=True)
class SummarySubgroupView:
    section_id: str
    name: str
    items: List[SummaryItemView]


@dataclass(frozen=True)
class SummaryGroupView:
    profile_id: str
    name: str
    items: List[SummaryItemView]
    subgroups: List[SummarySubgroupView] = field(default_factory=list)

    def buckets(self) -> List[SummarySubgroupView]:
        if self.subgroups:
            return list(self.subgroups)
        return [SummarySubgroupView(section_id="", name="", items=self.items)]


@dataclass(frozen=True)
class DailySummaryView:
    groups: List[SummaryGroupView]
    item_count: int


class DailySummarizer:
    """Generates daily Markdown summaries from pre-analyzed content items."""

    def __init__(
        self,
        profile_names: Optional[Dict[str, Dict[str, str]]] = None,
        profile_order: Optional[List[str]] = None,
        topic_sections: Optional[Dict[str, list]] = None,
    ):
        self.profile_names = profile_names or {}
        self.profile_order = profile_order or []
        self.topic_sections = topic_sections or {}

    @staticmethod
    def _profile_id(item: ContentItem) -> str:
        if item.processing:
            return item.processing.classification.profile
        return item.profile if isinstance(item.profile, str) else "unclassified"

    def profile_name(self, profile_id: str, language: str) -> str:
        names = self.profile_names.get(profile_id, {})
        return names.get(
            language,
            names.get(
                "default",
                profile_id.replace("-", " ").replace("_", " ").title(),
            ),
        )

    def build_view(
        self,
        items: List[ContentItem],
        language: str,
    ) -> DailySummaryView:
        grouped_items: Dict[str, List[ContentItem]] = {}
        for item in items:
            grouped_items.setdefault(self._profile_id(item), []).append(item)

        ordered_groups = list(grouped_items.items())
        if self.profile_order:
            order = {
                profile_id: index
                for index, profile_id in enumerate(self.profile_order)
            }
            ordered_groups = sorted(
                ordered_groups,
                key=lambda group: order.get(group[0], len(order)),
            )

        groups = []
        global_index = 1
        labels = LABELS.get(language, LABELS["en"])
        for profile_id, profile_items in ordered_groups:
            sections = self.topic_sections.get(profile_id) or []
            subgroups: List[SummarySubgroupView] = []
            if sections:
                known = {
                    str(self._section_value(section, "id"))
                    for section in sections
                }
                buckets: Dict[str, List[ContentItem]] = {
                    section_id: [] for section_id in known
                }
                unmatched: List[ContentItem] = []
                for item in profile_items:
                    section_id = self._matching_section_id(item, known)
                    if section_id is None:
                        unmatched.append(item)
                    else:
                        buckets[section_id].append(item)
                ordered_buckets = []
                for section in sections:
                    section_id = str(self._section_value(section, "id"))
                    if buckets[section_id]:
                        ordered_buckets.append(
                            (
                                section_id,
                                self._section_heading(section, language),
                                buckets[section_id],
                            )
                        )
                if unmatched:
                    ordered_buckets.append(
                        ("other", labels["other_section"], unmatched)
                    )
                flat_items: List[SummaryItemView] = []
                for section_id, heading, bucket_items in ordered_buckets:
                    view_items = []
                    for index, item in enumerate(bucket_items, start=1):
                        view_item = self._view_item(
                            item,
                            language,
                            index=index,
                            group_count=len(bucket_items),
                            global_index=global_index,
                            profile_id=profile_id,
                            section_id=section_id,
                        )
                        view_items.append(view_item)
                        flat_items.append(view_item)
                        global_index += 1
                    subgroups.append(
                        SummarySubgroupView(
                            section_id=section_id,
                            name=normalize_language(heading, language),
                            items=view_items,
                        )
                    )
                view_items = flat_items
            else:
                view_items = []
                for index, item in enumerate(profile_items, start=1):
                    view_items.append(
                        self._view_item(
                            item,
                            language,
                            index=index,
                            group_count=len(profile_items),
                            global_index=global_index,
                            profile_id=profile_id,
                        )
                    )
                    global_index += 1
            groups.append(
                SummaryGroupView(
                    profile_id=profile_id,
                    name=normalize_language(
                        self.profile_name(profile_id, language), language
                    ),
                    items=view_items,
                    subgroups=subgroups,
                )
            )
        return DailySummaryView(groups=groups, item_count=len(items))

    def _view_item(
        self,
        item: ContentItem,
        language: str,
        *,
        index: int,
        group_count: int,
        global_index: int,
        profile_id: str,
        section_id: Optional[str] = None,
    ) -> SummaryItemView:
        artifact = (
            item.processing.artifacts.get(language) if item.processing else None
        )
        analysis = item.processing.analysis if item.processing else None
        return SummaryItemView(
            item=item,
            index=index,
            global_index=global_index,
            group_count=group_count,
            title=normalize_language(
                artifact.title if artifact else item.title, language
            ),
            score=(
                analysis.score
                if analysis and analysis.score is not None
                else "?"
            ),
            anchor_id=self._item_anchor(profile_id, index, section_id),
        )

    @staticmethod
    def _section_value(section: object, key: str) -> object:
        if isinstance(section, dict):
            return section.get(key)
        return getattr(section, key)

    def _section_heading(self, section: object, language: str) -> str:
        names = self._section_value(section, "display_names") or {}
        if not isinstance(names, dict):
            names = {}
        return (
            names.get(language)
            or names.get("default")
            or self._section_value(section, "name")
            or self._section_value(section, "id")
            or ""
        )

    @staticmethod
    def _matching_section_id(
        item: ContentItem, section_ids: set[str]
    ) -> Optional[str]:
        """Prefer an explicit source category, then an analysis tag."""
        category = item.metadata.get("category")
        if isinstance(category, str) and category in section_ids:
            return category
        analysis = item.processing.analysis if item.processing else None
        if analysis is None:
            return None
        for tag in analysis.tags:
            normalized = re.sub(
                r"[^a-z0-9_-]+", "-", str(tag).strip().lower()
            ).strip("-")
            if normalized in section_ids:
                return normalized
        return None

    @staticmethod
    def _item_anchor(
        profile_id: str, index: int, section_id: Optional[str] = None
    ) -> str:
        safe_profile_id = re.sub(r"[^a-zA-Z0-9_-]+", "-", profile_id).strip("-")
        prefix = f"item-{safe_profile_id or 'unclassified'}"
        if section_id:
            safe_section_id = re.sub(r"[^a-zA-Z0-9_-]+", "-", section_id).strip("-")
            prefix = f"{prefix}-{safe_section_id or 'section'}"
        return f"{prefix}-{index}"

    @staticmethod
    def _render_label(text: str, language: str) -> str:
        rendered = _escape_markdown(text)
        if language == "zh":
            rendered = _pangu(rendered)
        return rendered

    @staticmethod
    def _score_suffix(view_item: SummaryItemView) -> str:
        if view_item.item.metadata.get("unscored"):
            return ""
        return f" \u2b50\ufe0f {view_item.score}/10"

    async def generate_summary(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate daily summary in Markdown format.

        Items are rendered in score-descending order (already sorted by orchestrator).

        Args:
            items: High-scoring content items (already enriched)
            date: Date string (YYYY-MM-DD)
            total_fetched: Total number of items fetched before filtering
            language: Output language, either "en" or "zh"

        Returns:
            str: Markdown formatted summary
        """
        labels = LABELS.get(language, LABELS["en"])

        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        header = (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['selected_items'].format(total=total_fetched, selected=len(items))}\n\n"
            "---\n\n"
        )

        toc_sections = []
        body_sections = []
        view = self.build_view(items, language)
        for group in view.groups:
            profile_name = self._render_label(group.name, language)
            toc_entries = [f"**{profile_name}**"]
            body_sections.append(f"## {profile_name}\n\n")
            heading_level = 4 if group.subgroups else 3
            for bucket in group.buckets():
                if bucket.name:
                    section_name = self._render_label(bucket.name, language)
                    toc_entries.extend(["", f"**{section_name}**"])
                    body_sections.append(f"### {section_name}\n\n")
                for view_item in bucket.items:
                    title = self._render_label(view_item.title, language)
                    toc_entries.append(
                        f"{view_item.index}. [{title}](#{view_item.anchor_id})"
                        f"{self._score_suffix(view_item)}"
                    )
                    body_sections.append(
                        self._format_item(
                            view_item.item,
                            labels,
                            language,
                            view_item.index,
                            heading_level=heading_level,
                            anchor_id=view_item.anchor_id,
                            title_override=view_item.title,
                            score_override=view_item.score,
                        )
                    )
            toc_sections.append("\n".join(toc_entries))

        toc = "\n\n".join(toc_sections) + "\n\n---\n\n"
        return normalize_language(header + toc + "".join(body_sections), language)

    def generate_webhook_overview(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate a compact overview for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        if language == "zh":
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> 从 {total_fetched} 条内容中筛选出 {len(items)} 条重要资讯。\n\n"
                "下面会按内容逐条发送详情，你可以只看感兴趣的标题。\n\n"
            )
        else:
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> Selected {len(items)} important items from {total_fetched} fetched items.\n\n"
                "Details will be sent item by item so you can read only the topics you care about.\n\n"
            )

        sections = []
        view = self.build_view(items, language)
        for group in view.groups:
            profile_name = self._render_label(group.name, language)
            entries = [f"**{profile_name}**"]
            for bucket in group.buckets():
                if bucket.name:
                    entries.extend(
                        ["", f"**{self._render_label(bucket.name, language)}**"]
                    )
                for view_item in bucket.items:
                    title = self._render_label(view_item.title, language)
                    url = _safe_url(view_item.item.url)
                    title_link = f"[{title}]({url})" if url else title
                    entries.append(
                        f"{view_item.index}. {title_link}"
                        f"{self._score_suffix(view_item)}"
                    )
            sections.append("\n".join(entries))

        return normalize_language(header + "\n\n".join(sections), language)

    def generate_webhook_item(
        self,
        item: ContentItem,
        language: str,
        index: int,
        total: int,
        *,
        title: Optional[str] = None,
        score: float | str | None = None,
    ) -> str:
        """Generate one item message for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        prefix = f"第 {index}/{total} 条\n\n" if language == "zh" else f"Item {index}/{total}\n\n"
        return normalize_language(
            prefix
            + self._format_item(
                item,
                labels,
                language,
                index,
                title_override=title,
                score_override=score,
            ).rstrip("-\n "),
            language,
        )

    def _format_item(
        self,
        item: ContentItem,
        labels: dict,
        language: str,
        index: int,
        *,
        heading_level: int = 2,
        anchor_id: Optional[str] = None,
        title_override: Optional[str] = None,
        score_override: float | str | None = None,
    ) -> str:
        """Format a single ContentItem into Markdown."""
        artifact = item.processing.artifacts.get(language) if item.processing else None
        analysis = item.processing.analysis if item.processing else None
        _title = title_override or (artifact.title if artifact else item.title)
        title = _escape_markdown(_title)
        raw_url = str(item.url)
        url = _safe_url(raw_url)
        score = (
            score_override
            if score_override is not None
            else analysis.score
            if analysis and analysis.score is not None
            else "?"
        )
        meta = item.metadata

        summary = analysis.summary if not artifact and analysis else ""
        primary_block = (
            next((block for block in artifact.blocks if block.primary), None)
            if artifact
            else None
        )

        summary = _escape_markdown(summary)
        primary_content = (
            _escape_markdown(primary_block.content) if primary_block else ""
        )

        if language == "zh":
            title = _pangu(title)
            summary = _pangu(summary)
            primary_content = _pangu(primary_content)

        # Source line with parts joined by " · ", link appended at end
        source_type = item.source_type.value
        source_parts = [_escape_markdown(source_type)]
        if meta.get("subreddit"):
            source_parts.append(_escape_markdown(f"r/{meta['subreddit']}"))
        if meta.get("feed_name"):
            source_parts.append(_escape_markdown(meta["feed_name"]))
        else:
            source_parts.append(_escape_markdown(item.author or "unknown"))
        if item.published_at:
            if language == "zh":
                source_parts.append(
                    f"{item.published_at.month}月{item.published_at.day}日 "
                    f"{item.published_at:%H:%M}"
                )
            else:
                day = item.published_at.strftime("%d").lstrip("0")
                source_parts.append(item.published_at.strftime(f"%b {day}, %H:%M"))
        source_line = " \u00b7 ".join(source_parts)  # ·

        discussion_url = meta.get("discussion_url")
        if discussion_url:
            safe_discussion_url = _safe_url(discussion_url)
            if safe_discussion_url and str(discussion_url) != raw_url:
                source_line += f' · [{labels["discussion"]}]({safe_discussion_url})'

        title_link = f"[{title}]({url})" if url else title
        score_suffix = (
            ""
            if item.metadata.get("unscored")
            else f" \u2b50\ufe0f {score}/10"
        )

        lines = [
            f'<a id="{anchor_id or f"item-{index}"}"></a>',
            f"{'#' * heading_level} {title_link}{score_suffix}",
        ]
        if summary.strip():
            lines.extend(["", summary])
        if primary_content.strip():
            lines.extend(["", primary_content])
        lines.extend(["", source_line])

        if artifact:
            for block in artifact.blocks:
                if block.primary:
                    continue
                block_title = _escape_markdown(block.title)
                block_content = _escape_markdown(block.content)
                if language == "zh":
                    block_title = _pangu(block_title)
                    block_content = _pangu(block_content)
                lines.extend(["", f"**「{block_title}」** {block_content}"])

        sources = artifact.sources if artifact else []
        if sources:
            reference_items = []
            for source in sources:
                reference_title = html.escape(source.title, quote=True)
                reference_url = _safe_url(source.url)
                if reference_url:
                    reference_items.append(f'<li><a href="{reference_url}">{reference_title}</a></li>\n')
                else:
                    reference_items.append(f"<li>{reference_title}</li>\n")
            items_html = "".join(reference_items)
            lines += [
                "",
                f'<details><summary>{labels["references"]}</summary>\n<ul>\n{items_html}\n</ul>\n</details>',
            ]

        if analysis and analysis.tags:
            tags_str = ", ".join([f"`#{_escape_markdown(t)}`" for t in analysis.tags])
            lines.append("")
            lines.append(f"**{labels['tags']}**: {tags_str}")

        lines.append("")
        lines.append("---")

        return "\n".join(lines) + "\n\n"

    def _generate_empty_summary(self, date: str, total_fetched: int, labels: dict) -> str:
        """Generate summary when no high-scoring items were found."""
        return (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['empty_analyzed'].format(total=total_fetched)}\n\n"
            + labels["empty_body"]
        )

"""Per-profile collection windows.

``collection.time_window_hours`` stays the default. A profile may set its own
window. A source is fetched with the widest window among the profiles it can
route to. An item is then kept only for profiles whose window still contains
its publication time, so a dual-profile source cannot place an older item in
a shorter section.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Callable, Iterable, Mapping, Sequence, TypeVar

from ..models import ContentItem, ProfileRoute, ProfileSettingsConfig

T = TypeVar("T")


def default_window_hours(collection_hours: int, force_hours: int | None) -> int:
    """Return the window used by profiles that do not set their own.

    A truthy ``force_hours`` (the ``--hours`` flag) replaces the configured
    default. Zero and ``None`` keep the configured default. An explicit
    profile window is applied separately and is not replaced here.
    """
    if force_hours:
        return force_hours
    return collection_hours


def profile_window_hours(
    profile_id: str,
    settings: Mapping[str, ProfileSettingsConfig],
    default_hours: int,
) -> int:
    """Return one profile's window, or the default when it has none."""
    profile_settings = settings.get(profile_id)
    if profile_settings is not None and profile_settings.time_window_hours is not None:
        return profile_settings.time_window_hours
    return default_hours


def routable_profile_ids(route: ProfileRoute, known_ids: Sequence[str]) -> list[str]:
    """Profiles a source route may resolve to.

    A missing route or ``auto`` can resolve to any known profile. A string or
    candidate list is used as written.
    """
    if route is None:
        return list(known_ids)
    if isinstance(route, str):
        normalized = route.strip() or "auto"
        if normalized == "auto":
            return list(known_ids)
        return [normalized]
    return [profile_id.strip() for profile_id in route]


def fetch_hours_for_route(
    route: ProfileRoute,
    known_ids: Sequence[str],
    window_for: Callable[[str], int],
    default_hours: int,
) -> int:
    """Widest window among the profiles this route can still reach."""
    profile_ids = routable_profile_ids(route, known_ids)
    if not profile_ids:
        return default_hours
    return max(window_for(profile_id) for profile_id in profile_ids)


def aware(moment: datetime) -> datetime:
    """Treat a naive timestamp as UTC, matching the RSS scraper."""
    if moment.tzinfo is None:
        return moment.replace(tzinfo=timezone.utc)
    return moment


def accepts_published_at(published_at: datetime, now: datetime, hours: int) -> bool:
    """True when the item is inside the window, including the exact cutoff."""
    cutoff = aware(now) - timedelta(hours=hours)
    return aware(published_at) >= cutoff


def restrict_route(
    route: ProfileRoute,
    published_at: datetime,
    *,
    now: datetime,
    known_ids: Sequence[str],
    window_for: Callable[[str], int],
) -> tuple[bool, ProfileRoute]:
    """Return whether to keep the item, and the route that may still receive it.

    One remaining profile is returned as a string so classification uses that
    profile directly. Several remaining candidates stay a list. ``(False, _)``
    means every routable profile rejects the item's age.
    """
    requested = routable_profile_ids(route, known_ids)
    eligible = [
        profile_id
        for profile_id in requested
        if accepts_published_at(published_at, now, window_for(profile_id))
    ]
    if not eligible:
        return False, route
    if len(eligible) == 1:
        return True, eligible[0]
    open_route = route is None or (
        isinstance(route, str) and (route.strip() or "auto") == "auto"
    )
    if open_route and eligible == list(known_ids):
        return True, route
    if (
        not open_route
        and isinstance(route, list)
        and [profile_id.strip() for profile_id in route] == eligible
    ):
        return True, route
    return True, eligible


def restrict_items(
    items: Iterable[ContentItem],
    *,
    now: datetime,
    known_ids: Sequence[str],
    window_for: Callable[[str], int],
) -> list[ContentItem]:
    """Drop items outside every routable window and narrow the rest."""
    kept: list[ContentItem] = []
    for item in items:
        keep, route = restrict_route(
            item.profile,
            item.published_at,
            now=now,
            known_ids=known_ids,
            window_for=window_for,
        )
        if not keep:
            continue
        if route is not item.profile:
            item.profile = route
        kept.append(item)
    return kept


def resolved_profile_accepts(
    item: ContentItem,
    *,
    now: datetime,
    default_profile: str,
    window_for: Callable[[str], int],
) -> bool:
    """False when the already chosen profile's window excludes the item."""
    if item.processing and item.processing.classification:
        profile_id = item.processing.classification.profile
    elif isinstance(item.profile, str) and item.profile.strip() not in {"", "auto"}:
        profile_id = item.profile.strip()
    else:
        profile_id = default_profile
    return accepts_published_at(item.published_at, now, window_for(profile_id))


def group_by_fetch_hours(
    entries: Iterable[T],
    route_of: Callable[[T], ProfileRoute],
    hours_for: Callable[[ProfileRoute], int | None],
) -> dict[int | None, list[T]]:
    """Group source entries by the window they should be fetched with.

    ``None`` means "use the caller's single cutoff" and is the key used when
    per-profile windows are not applied.
    """
    grouped: dict[int | None, list[T]] = {}
    for entry in entries:
        grouped.setdefault(hours_for(route_of(entry)), []).append(entry)
    return grouped

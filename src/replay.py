"""Decide whether a run may publish, and refuse historical mislabels.

A live collection always reads the last N hours from the current clock. Naming
that output with an earlier Asia/Shanghai date would replace a published page
with today's sources. Scheduled runs never take a requested date.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


class ReplayRefusal(ValueError):
    """The requested command would mislabel or publish a historical digest."""


def parse_digest_date(value: str) -> str:
    """Return a normalized YYYY-MM-DD date, or raise ReplayRefusal."""
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise ReplayRefusal(
            f"digest date must be YYYY-MM-DD, got {value!r}"
        ) from exc
    return parsed.isoformat()


def resolve_cli_action(
    *,
    requested_date: str | None,
    dry_run: bool,
    from_published: str | None,
    shanghai_today: str,
) -> str:
    """Return ``live``, ``live-dry-run``, or ``published-replay``.

    A date other than Shanghai today cannot drive a live fetch. The published
    page has to be supplied, and the command has to be a dry run.
    """
    if requested_date is None:
        return "live-dry-run" if dry_run else "live"
    digest_date = parse_digest_date(requested_date)
    if digest_date == shanghai_today:
        return "live-dry-run" if dry_run else "live"
    if not dry_run:
        raise ReplayRefusal(
            f"Refusing to publish a live collection as {digest_date}. "
            f"Asia/Shanghai today is {shanghai_today}. A live fetch uses the "
            "last N hours from now and would overwrite that historical page "
            "with current sources. Re-run only with --dry-run and "
            "--from-published pointing at the already published page."
        )
    if not from_published:
        raise ReplayRefusal(
            f"{digest_date} is not today. A dry run of a past date must use "
            "--from-published and does not fetch RSS."
        )
    return "published-replay"


@dataclass(frozen=True)
class DigestRunPlan:
    mode: str
    digest_date: str
    run_live_horizon: bool
    publish: bool
    dry_run: bool


def plan_digest_run(
    *,
    event: str,
    shanghai_today: str,
    requested_date: str | None,
    dry_run: bool,
) -> DigestRunPlan:
    """Plan a workflow run. Schedule events ignore requested dates and dry-run."""
    today = parse_digest_date(shanghai_today)
    if event != "workflow_dispatch":
        return DigestRunPlan(
            mode="scheduled-live",
            digest_date=today,
            run_live_horizon=True,
            publish=True,
            dry_run=False,
        )
    requested = (requested_date or "").strip()
    if requested and parse_digest_date(requested) != today:
        return DigestRunPlan(
            mode="historical-preview",
            digest_date=parse_digest_date(requested),
            run_live_horizon=False,
            publish=False,
            dry_run=True,
        )
    if dry_run:
        return DigestRunPlan(
            mode="dry-run",
            digest_date=today,
            run_live_horizon=True,
            publish=False,
            dry_run=True,
        )
    return DigestRunPlan(
        mode="manual-live",
        digest_date=today,
        run_live_horizon=True,
        publish=True,
        dry_run=False,
    )

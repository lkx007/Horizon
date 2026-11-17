"""Calendar date for Horizon digest files and Pages posts.

Filenames use Asia/Shanghai. Between 00:00 and 08:00 Shanghai the UTC date
is still the previous day, so an overnight run writes today's name only when
the digest date comes from this module.
"""

from datetime import date, datetime
from zoneinfo import ZoneInfo

DIGEST_TZ = ZoneInfo("Asia/Shanghai")


def digest_calendar_date(moment: datetime | None = None) -> date:
    """Return the digest calendar date in Asia/Shanghai."""
    if moment is None:
        moment = datetime.now(DIGEST_TZ)
    elif moment.tzinfo is None:
        raise ValueError("digest date requires an aware datetime")
    return moment.astimezone(DIGEST_TZ).date()


def digest_date_str(moment: datetime | None = None) -> str:
    """Return the digest calendar date as ``YYYY-MM-DD`` in Asia/Shanghai."""
    return digest_calendar_date(moment).isoformat()

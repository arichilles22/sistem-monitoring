import calendar
from datetime import datetime
import typing as t
from click import DateTime
from markupsafe import Markup
import re

WEEKDAYSLIST = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]


def truncate(
    s: str,
    length: int = 255,
    killwords: bool = False,
    end: str = "...",
    leeway: t.Optional[int] = None,
) -> str:
    """Mengembalikan nilai string yang panjang karakternya dapat ditetukan.
    Panjang karakternya ditentukan dengan parameter ``length`` dengan nilai
    defaultnya ``255``. Jika parameter kedua ``killword`` adalah ``true``
    maka panjang teks akan dipotong, jika bernilai ``false`` maka akan membuang
    kata terakhir. Jika teks teks itu dipotong amaka akan menambahkan tanda elipsi (``"..."``)
    """
    if leeway is None:
        leeway = 5
    assert length >= len(end), f"expected length >= {len(end)}, got {length}"
    assert leeway >= 0, f"expected leeway >/ 0, got {leeway}"

    if len(s) <= length + leeway:
        return s

    if killwords:
        return s[: length - len(end)] + end
    result = s[: length - len(end)].rsplit(" ", 1)[0]

    return result


def safe(s: str) -> Markup:
    """Mark a value as unsafe.  This is the reverse operation for :func:`safe`."""
    return Markup(str)


def remove_tag(s: str) -> str:
    clean = re.compile("<.*?>")
    return re.sub(clean, "", s)


def from_db(date: datetime):
    str_date = str(date)
    # new_str = "/".join(str_date.split("-"))
    new_str = (
        f"{str_date.split('-')[0]}/{str_date.split('-')[1]}/{str_date.split('-')[2]}"
    )

    return new_str


def hari_sabtu(date: datetime):
    week_day = calendar.weekday(date.year, date.month, date.day)

    if week_day == 5:
        return WEEKDAYSLIST[week_day]

    return None


def hari_minggu(date: datetime):
    week_day = calendar.weekday(date.year, date.month, date.day)

    if week_day == 6:
        return WEEKDAYSLIST[week_day]

    return None

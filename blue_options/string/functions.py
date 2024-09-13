from typing import Union, Any, List
import datetime
import numpy as np
from datetime import timezone
import math
import random as random_module
import string as string_module
import time

from blueness import module

from blue_options import NAME
from blue_options.string.constants import unit_of
from blue_options.logger import logger


NAME = module.name(__file__, NAME)


def after(
    s: str,
    sub_string: str,
    n: int = 1,
):
    if sub_string == "" or sub_string not in s:
        return ""

    return sub_string.join(s.split(sub_string)[n:])


def before(
    s: str,
    sub_string: str,
    n: int = 1,
):
    if sub_string == "" or sub_string not in s:
        return ""

    return sub_string.join(s.split(sub_string)[:n])


def between(
    s: str,
    sub_string_1: str,
    sub_string_2: str,
):
    return before(
        after(
            s,
            sub_string_1,
        ),
        sub_string_2,
    )


def pretty_bytes(
    byte_count: Union[None, int],
) -> str:
    if byte_count is None:
        return "Unknown"

    byte_count = round(byte_count)

    # Less than a kB
    if byte_count < 1024 / 10:
        return f"{byte_count:.0f} byte(s)"

    byte_count /= 1024

    if byte_count < 1024 / 10:
        return f"{byte_count:.2f} kB"

    byte_count /= 1024

    if byte_count < 1024:
        return f"{byte_count:.2f} MB"

    byte_count /= 1024

    if byte_count < 1024:
        return f"{byte_count:.2f} GB"

    byte_count /= 1024

    return f"{byte_count:.2f} TB"


def pretty_date(
    date: Any = None,
    as_filename: bool = False,
    delimiter: str = ", ",
    explicit_format: str = "",
    in_gmt: bool = False,
    include_date: bool = True,
    include_seconds: bool = True,
    include_time: bool = True,
    include_weekdays: bool = False,
    include_zone: bool = False,
    short: bool = False,
    squeeze: bool = False,
    unique: bool = False,
) -> str:
    format = ""
    if include_date:
        if short or as_filename:
            format = "%Y %m %d"
        else:
            format = "%d %B %Y"

        if include_weekdays:
            format = "%A, " + format

        if include_time:
            format += delimiter
    if include_time:
        format += "%H:%M"
        if include_seconds:
            format += ":%S"
    if unique:
        format += f":{random_module.randrange(100000):05d}"
    if as_filename:
        format = (
            format.replace(" ", "-")
            .replace(":", "-")
            .replace(".", "-")
            .replace(",", "")
        )

    if explicit_format:
        format = explicit_format

    if date is None:
        date = time.time()
    if isinstance(date, datetime.datetime):
        output = date.strftime(format)
    else:
        if in_gmt:
            output = time.strftime(format, time.gmtime(date))

            if include_zone:
                output += " (GMT)"
        else:
            output = time.strftime(format, time.localtime(date))

            if include_zone:
                output += f" ({time.tzname[0] if time.tzname else '?'})"

    if squeeze:
        output = output.replace("-", "")

    return output


def pretty_frequency(
    frequency: Union[None, float],
) -> str:
    if frequency is None or frequency == 0:
        return "None"

    if frequency >= 0.5:
        if frequency < 10**3:
            return f"{frequency:.1f} Hz"

        if frequency < 10**6:
            return f"{frequency / 10**3:.1f} kHz"

        if frequency < 10**6:
            return f"{frequency / 10**6:.1f} MHz"

        return f"{frequency / 10**9:.1f} GHz"

    return "1/{}".format(
        pretty_duration(
            1 / frequency,
            largest=True,
            short=True,
        )
    )


def pretty_shape(shape: List[int]) -> str:
    return "x".join([str(value) for value in list(shape)])


def pretty_shape_of_matrix(
    matrix: np.ndarray,
) -> str:
    return (
        f"{pretty_shape(matrix.shape)}:{matrix.dtype}"
        if isinstance(matrix, np.ndarray)
        else "-"
    )


def pretty_duration(
    duration: Union[None, int],
    element_format: str = "{}{}",
    include_ms: bool = False,
    largest: bool = False,
    past: bool = False,
    short: bool = False,
) -> str:
    if duration is None:
        return "None"

    negative_duration = duration < 0
    duration = abs(duration)

    duration_ = duration
    duration = math.floor(duration) if include_ms else round(duration)

    milliseconds = round(1000 * (duration_ - duration))

    seconds = duration % 60
    duration = math.floor(duration / 60)
    minutes = duration % 60
    duration = math.floor(duration / 60)
    hours = duration % 24
    duration = math.floor(duration / 24)
    days = duration % 30
    duration = math.floor(duration / 30)
    months = duration % 12
    years = math.floor(duration / 12)

    if short:
        year_name = " yr"
        month_name = " mth"
        day_name = " d"
        hour_name = " hr"
        minute_name = " min"
        second_name = " s"
        millisecond_name = " ms"
    else:
        year_name = " year(s)"
        month_name = " month(s)"
        day_name = " day(s)"
        hour_name = " hour(s)"
        minute_name = " minute(s)"
        second_name = " second(s)"
        millisecond_name = " millisecond(s)"

    output = []
    if years > 0:
        output.append(element_format.format(years, year_name))
    if months > 0:
        output.append(element_format.format(months, month_name))
    if days > 0:
        output.append(element_format.format(days, day_name))
    if hours > 0:
        output.append(element_format.format(hours, hour_name))
    if minutes > 0:
        output.append(element_format.format(minutes, minute_name))
    if seconds > 0:
        output.append(element_format.format(seconds, second_name))
    if include_ms:
        if milliseconds > 0:
            output.append("{:03d}{}".format(milliseconds, millisecond_name))

    if largest:
        output = output[:1]
    output = ", ".join(output)

    if past and output:
        output += " ago"

    if not output:
        output = "< 1{}".format(millisecond_name if include_ms else second_name)

    return ("-" if negative_duration else "") + output


def random(
    length: int = 16,
    alphabet: str = string_module.ascii_lowercase
    + string_module.digits
    + string_module.ascii_uppercase,
):
    return "".join(random_module.choice(alphabet) for _ in range(length))


def timestamp() -> str:
    return pretty_date(
        as_filename=True,
        include_time=True,
        unique=True,
    )


def utc_timestamp(
    date: Any = None,
    format: str = "%Y-%m-%d-%H-%M-%S",
    timezone_: str = "America/New_York",
) -> str:
    if date is None:
        # https://www.geeksforgeeks.org/get-utc-timestamp-in-python/
        return (
            datetime.datetime.now(timezone.utc).replace(tzinfo=timezone.utc).timestamp()
        )

    try:
        # https://stackoverflow.com/a/79877/17619982
        import pytz

        local = pytz.timezone(timezone_)
        naive = datetime.datetime.strptime(date, format)
        local_dt = local.localize(naive, is_dst=None)
        return local_dt.astimezone(pytz.utc).timestamp()
    except:
        logger.error(f"{NAME}.utc_timestamp({date},{format}): failed.")
        return "unknown"

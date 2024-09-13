import os
import time

# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
os.environ["TZ"] = "America/Vancouver"
time.tzset()

from blue_options.string.constants import unit_of
from blue_options.string.functions import (
    after,
    before,
    between,
    pretty_bytes,
    pretty_date,
    pretty_duration,
    pretty_frequency,
    pretty_shape,
    pretty_shape_of_matrix,
    random,
    timestamp,
    utc_timestamp,
)

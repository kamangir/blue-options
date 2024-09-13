from typing import Callable, Any, Union, List
import pytest
import numpy as np

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


@pytest.mark.parametrize(
    [
        "s",
        "sub_string",
        "n",
        "expected_output",
    ],
    [
        [
            "this is a test",
            "",
            1,
            "",
        ],
        [
            "this is a test",
            "was",
            1,
            "",
        ],
        [
            "this is a test",
            "is",
            1,
            " is a test",
        ],
        [
            "this is a test that is very important",
            "is",
            1,
            " is a test that is very important",
        ],
        [
            "this is a test that is very important",
            "is",
            2,
            " a test that is very important",
        ],
        [
            "this is a test that is very important",
            "is",
            3,
            " very important",
        ],
        [
            "this is a test that is very important",
            "is",
            4,
            "",
        ],
        [
            "this is a test that is very important",
            "is",
            45,
            "",
        ],
        [
            "this is a test that is very important and now is running",
            "is",
            1,
            " is a test that is very important and now is running",
        ],
        [
            "this is a test that is very important and now is running",
            "is",
            2,
            " a test that is very important and now is running",
        ],
        [
            "this is a test that is very important and now is running",
            "is",
            3,
            " very important and now is running",
        ],
    ],
)
def test_string_after(
    s: str,
    sub_string: str,
    n: int,
    expected_output: str,
):
    assert after(s, sub_string, n) == expected_output

    if n == 1:
        assert after(s, sub_string) == expected_output


@pytest.mark.parametrize(
    [
        "s",
        "sub_string",
        "n",
        "expected_output",
    ],
    [
        [
            "this is a test",
            "",
            1,
            "",
        ],
        [
            "this is a test",
            "was",
            1,
            "",
        ],
        [
            "this is a test",
            "is",
            1,
            "th",
        ],
        [
            "this is a test that is very important",
            "is",
            1,
            "th",
        ],
        [
            "this is a test that is very important",
            "is",
            2,
            "this ",
        ],
        [
            "this is a test that is very important and now is running",
            "is",
            1,
            "th",
        ],
        [
            "this is a test that is very important and now is running",
            "is",
            2,
            "this ",
        ],
        [
            "this is a test that is very important and now is running",
            "is",
            3,
            "this is a test that ",
        ],
        [
            "this is a test that is very important and now is running",
            "is",
            450,
            "this is a test that is very important and now is running",
        ],
    ],
)
def test_string_before(
    s: str,
    sub_string: str,
    n: int,
    expected_output: str,
):
    assert before(s, sub_string, n) == expected_output

    if n == 1:
        assert before(s, sub_string) == expected_output


def test_string_between():
    assert isinstance(
        between(
            random(10),
            random(10),
            random(10),
        ),
        str,
    ), "test by simplicity of the logic 🪄."


@pytest.mark.parametrize(
    ["byte_count", "expected_output"],
    [
        [0, "0 byte(s)"],
        [1, "1 byte(s)"],
        [2, "2 byte(s)"],
        [4, "4 byte(s)"],
        [8, "8 byte(s)"],
        [16, "16 byte(s)"],
        [32, "32 byte(s)"],
        [64, "64 byte(s)"],
        [128, "0.12 kB"],
        [256, "0.25 kB"],
        [512, "0.50 kB"],
        [1024, "1.00 kB"],
        [2048, "2.00 kB"],
        [4096, "4.00 kB"],
        [8192, "8.00 kB"],
        [16384, "16.00 kB"],
        [32768, "32.00 kB"],
        [65536, "64.00 kB"],
        [131072, "0.12 MB"],
        [262144, "0.25 MB"],
        [524288, "0.50 MB"],
        [1048576, "1.00 MB"],
        [2097152, "2.00 MB"],
        [4194304, "4.00 MB"],
        [8388608, "8.00 MB"],
        [16777216, "16.00 MB"],
        [33554432, "32.00 MB"],
        [67108864, "64.00 MB"],
        [134217728, "128.00 MB"],
        [268435456, "256.00 MB"],
        [536870912, "512.00 MB"],
        [1073741824, "1.00 GB"],
        [2147483648, "2.00 GB"],
        [4294967296, "4.00 GB"],
        [8589934592, "8.00 GB"],
        [17179869184, "16.00 GB"],
        [34359738368, "32.00 GB"],
        [68719476736, "64.00 GB"],
        [137438953472, "128.00 GB"],
        [274877906944, "256.00 GB"],
        [549755813888, "512.00 GB"],
        [1099511627776, "1.00 TB"],
        [2199023255552, "2.00 TB"],
        [4398046511104, "4.00 TB"],
        [8796093022208, "8.00 TB"],
        [17592186044416, "16.00 TB"],
        [35184372088832, "32.00 TB"],
        [70368744177664, "64.00 TB"],
        [140737488355328, "128.00 TB"],
        [281474976710656, "256.00 TB"],
        [562949953421312, "512.00 TB"],
    ],
)
def test_string_pretty_bytes(
    byte_count: int,
    expected_output: str,
):
    assert pretty_bytes(byte_count) == expected_output


@pytest.mark.parametrize(["date"], [[None]])
@pytest.mark.parametrize(["as_filename"], [[True], [False]])
@pytest.mark.parametrize(["explicit_format"], [[""], ["%d %B %Y"]])
@pytest.mark.parametrize(["in_gmt"], [[True], [False]])
@pytest.mark.parametrize(["include_date"], [[True], [False]])
@pytest.mark.parametrize(["include_seconds"], [[True], [False]])
@pytest.mark.parametrize(["include_time"], [[True], [False]])
@pytest.mark.parametrize(["include_weekdays"], [[True], [False]])
@pytest.mark.parametrize(["include_zone"], [[True], [False]])
@pytest.mark.parametrize(["short"], [[True], [False]])
@pytest.mark.parametrize(["squeeze"], [[True], [False]])
@pytest.mark.parametrize(["unique"], [[True], [False]])
def test_string_pretty_date(
    date: Any,
    as_filename: bool,
    explicit_format: str,
    in_gmt: bool,
    include_date: bool,
    include_seconds: bool,
    include_time: bool,
    include_weekdays: bool,
    include_zone: bool,
    short: bool,
    squeeze: bool,
    unique: bool,
):
    assert isinstance(
        pretty_date(
            date=date,
            as_filename=as_filename,
            explicit_format=explicit_format,
            in_gmt=in_gmt,
            include_date=include_date,
            include_seconds=include_seconds,
            include_time=include_time,
            include_weekdays=include_weekdays,
            include_zone=include_zone,
            short=short,
            squeeze=squeeze,
            unique=unique,
        ),
        str,
    )


@pytest.mark.parametrize(["duration"], [[None], [12]])
@pytest.mark.parametrize(["include_ms"], [[True], [False]])
@pytest.mark.parametrize(["largest"], [[True], [False]])
@pytest.mark.parametrize(["past"], [[True], [False]])
@pytest.mark.parametrize(["short"], [[True], [False]])
def test_string_pretty_duration_options(
    duration: Union[None, int],
    include_ms: bool,
    largest: bool,
    past: bool,
    short: bool,
):
    assert isinstance(
        pretty_duration(
            duration=duration,
            include_ms=include_ms,
            largest=largest,
            past=past,
            short=short,
        ),
        str,
    )


@pytest.mark.parametrize(
    ["duration", "expected_output"],
    [
        [1, "1 second(s)"],
        [2, "2 second(s)"],
        [4, "4 second(s)"],
        [8, "8 second(s)"],
        [16, "16 second(s)"],
        [32, "32 second(s)"],
        [64, "1 minute(s)"],
        [128, "2 minute(s)"],
        [256, "4 minute(s)"],
        [512, "8 minute(s)"],
        [1024, "17 minute(s)"],
        [2048, "34 minute(s)"],
        [4096, "1 hour(s)"],
        [8192, "2 hour(s)"],
        [16384, "4 hour(s)"],
        [32768, "9 hour(s)"],
        [65536, "18 hour(s)"],
        [131072, "1 day(s)"],
        [262144, "3 day(s)"],
        [524288, "6 day(s)"],
        [1048576, "12 day(s)"],
        [2097152, "24 day(s)"],
        [4194304, "1 month(s)"],
        [8388608, "3 month(s)"],
        [16777216, "6 month(s)"],
        [33554432, "1 year(s)"],
        [67108864, "2 year(s)"],
        [134217728, "4 year(s)"],
        [268435456, "8 year(s)"],
        [536870912, "17 year(s)"],
    ],
)
def test_string_pretty_duration(
    duration: int,
    expected_output: str,
):
    assert (
        pretty_duration(
            duration,
            largest=True,
        )
        == expected_output
    )


@pytest.mark.parametrize(
    ["frequency", "expected_output"],
    [
        [None, "None"],
        [0, "None"],
        [1, "1.0 Hz"],
        [2, "2.0 Hz"],
        [4, "4.0 Hz"],
        [8, "8.0 Hz"],
        [16, "16.0 Hz"],
        [32, "32.0 Hz"],
        [64, "64.0 Hz"],
        [128, "128.0 Hz"],
        [256, "256.0 Hz"],
        [512, "512.0 Hz"],
        [1024, "1.0 kHz"],
        [2048, "2.0 kHz"],
        [4096, "4.1 kHz"],
        [8192, "8.2 kHz"],
        [16384, "16.4 kHz"],
        [32768, "32.8 kHz"],
        [65536, "65.5 kHz"],
        [131072, "131.1 kHz"],
        [262144, "262.1 kHz"],
        [524288, "524.3 kHz"],
        [1048576, "0.0 GHz"],
        [2097152, "0.0 GHz"],
        [4194304, "0.0 GHz"],
        [8388608, "0.0 GHz"],
        [16777216, "0.0 GHz"],
        [33554432, "0.0 GHz"],
        [67108864, "0.1 GHz"],
        [134217728, "0.1 GHz"],
        [268435456, "0.3 GHz"],
        [536870912, "0.5 GHz"],
        [1073741824, "1.1 GHz"],
        [2147483648, "2.1 GHz"],
        [4294967296, "4.3 GHz"],
        [8589934592, "8.6 GHz"],
        [17179869184, "17.2 GHz"],
        [34359738368, "34.4 GHz"],
        [68719476736, "68.7 GHz"],
        [137438953472, "137.4 GHz"],
        [274877906944, "274.9 GHz"],
        [549755813888, "549.8 GHz"],
    ],
)
def test_pretty_frequency(
    frequency: Union[float, None],
    expected_output: str,
):
    assert pretty_frequency(frequency) == expected_output


@pytest.mark.parametrize(
    ["shape", "expected_output"],
    [
        [[], ""],
        [[1], "1"],
        [[1, 2], "1x2"],
        [[1, 2, 3], "1x2x3"],
    ],
)
def test_pretty_shape(
    shape: List[int],
    expected_output: str,
):
    assert pretty_shape(shape) == expected_output


@pytest.mark.parametrize(
    [
        "matrix",
        "expected_output",
    ],
    [
        [
            np.array([]),
            "0:float64",
        ],
        [
            np.zeros((7), dtype=np.uint16),
            "7:uint16",
        ],
        [
            np.zeros((1, 2), dtype=np.float32),
            "1x2:float32",
        ],
        [
            np.zeros((1, 2, 3), dtype=np.uint8),
            "1x2x3:uint8",
        ],
    ],
)
def test_pretty_shape_of_matrix(
    matrix: np.ndarray,
    expected_output: str,
):
    assert pretty_shape_of_matrix(matrix) == expected_output


@pytest.mark.parametrize(
    ["func"],
    [
        [timestamp],
        [utc_timestamp],
    ],
)
def test_string_timestamp(func: Callable):
    isinstance(func(), str)


def test_string_uint_of():
    assert isinstance(unit_of, dict)

    for key, value in unit_of.items():
        assert isinstance(key, str)
        assert isinstance(value, str)

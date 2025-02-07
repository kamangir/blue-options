import os
from typing import Any
import pytest

from blue_options import string
from blue_options.env import get_env


@pytest.mark.parametrize(
    ["name"],
    [
        ["ABCLI_TEST_VARIABLE-{}".format(string.timestamp())],
    ],
)
@pytest.mark.parametrize(
    ["value", "default", "expected_value"],
    [
        ["some_value", "xyz", "some_value"],
        #
        ["12", 1, 12],
        ["void", 1, 1],
        #
        ["12.3", 1.0, 12.3],
        ["void", 1.0, 1.0],
        #
        ["1", True, True],
        ["0", True, False],
        ["1", False, True],
        ["0", False, False],
        ["void", True, False],
        ["void", False, False],
    ],
)
def test_env_get_env(
    name: str,
    value: str,
    default: Any,
    expected_value: Any,
):
    os.environ[name] = value

    value_as_is = get_env(name, default)
    assert value_as_is == expected_value

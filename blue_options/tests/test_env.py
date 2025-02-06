from typing import Any
import pytest

from blue_options.env import get_env


@pytest.mark.parametrize(
    ["name", "default"],
    [
        ["some_name", "some_value"],
        ["some_name", 1],
        ["some_name", 1.0],
        ["some_name", True],
    ],
)
def test_env_get_env(name: str, default: Any):
    value = get_env(name, default)
    assert isinstance(value, type(default))

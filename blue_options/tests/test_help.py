import pytest

from blue_options.help.registry import get_module_name


@pytest.mark.parametrize(
    ["callable", "expected_module_name"],
    [
        ["abcli_git", "abcli"],
        ["void_xyz", "void_xyz"],
    ],
)
def test_get_module_name(
    callable: str,
    expected_module_name: str,
):
    assert get_module_name(callable) == expected_module_name

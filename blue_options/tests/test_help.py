import pytest

from blue_options.help.parsing import get_callable_module, get_callable_suffix


@pytest.mark.parametrize(
    ["callable", "expected_module_name"],
    [
        ["abcli_git", "abcli"],
        ["abcli_git_push", "abcli"],
        ["void_xyz", "void_xyz"],
        ["void_xyz_abc_dddsf", "void_xyz_abc_dddsf"],
    ],
)
def test_get_callable_module(
    callable: str,
    expected_module_name: str,
):
    assert get_callable_module(callable) == expected_module_name


@pytest.mark.parametrize(
    ["callable", "expected_suffix"],
    [
        ["abcli_git", "git"],
        ["abcli_git_push", "git_push"],
        ["void_xyz", ""],
        ["void_xyz_abc_dddsf", ""],
    ],
)
def test_get_callable_suffix(
    callable: str,
    expected_suffix: str,
):
    assert get_callable_suffix(callable) == expected_suffix

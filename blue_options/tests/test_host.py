import pytest
from typing import Callable, Union
from blue_options.host.functions import (
    is_aws_batch,
    is_docker,
    is_ec2,
    is_github_workflow,
    is_headless,
    is_jetson,
    is_jupyter,
    is_mac,
    is_rpi,
    is_ubuntu,
)


@pytest.mark.parametrize(
    ["func", "expected_value"],
    [
        [is_aws_batch, None],
        [is_docker, None],
        [is_ec2, None],
        [is_github_workflow, None],
        [is_headless, False],
        [is_jetson, False],
        [is_jupyter, False],
        [is_mac, None],
        [is_rpi, False],
        [is_ubuntu, None],
    ],
)
def test_host_is(
    func: Callable,
    expected_value: Union[bool, None],
):
    if expected_value == True:
        assert func()
    elif expected_value == False:
        assert not func()
    elif expected_value == None:
        assert isinstance(func(), bool)
    else:
        assert False, "Invalid expected_value"

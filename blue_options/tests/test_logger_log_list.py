import pytest

from blue_options.logger import logger, log_list
from blue_options import string


@pytest.mark.parametrize(
    ["list_of_items"],
    [
        [[string.random(10) for _ in range(3)]],
        [[string.random(100) for _ in range(5)]],
        [[string.random(1000) for _ in range(10)]],
    ],
)
@pytest.mark.parametrize(
    ["max_length"],
    [
        [11],
        [51],
        [101],
    ],
)
@pytest.mark.parametrize(
    ["max_count"],
    [
        [1],
        [2],
        [5],
    ],
)
def test_log_list(
    list_of_items: str,
    max_length: int,
    max_count: int,
):
    log_list(
        logger=logger,
        list_of_items=list_of_items,
        max_count=max_count,
        max_length=max_length,
    )

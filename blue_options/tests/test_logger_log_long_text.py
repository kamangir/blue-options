import pytest

from blue_options.logger import logger, log_long_text
from blue_options import string


@pytest.mark.parametrize(
    ["text"],
    [
        [string.random(10)],
        [string.random(100)],
        [string.random(1000)],
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
def test_log_long_text(
    text: str,
    max_length: int,
):
    log_long_text(
        logger=logger,
        text=text,
        max_length=max_length,
    )

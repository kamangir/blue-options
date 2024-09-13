import pytest
from blue_options.host.functions import (
    get_name_,
    get_name,
    get_seed_filename,
    signature,
    tensor_processing_signature,
)


def test_host_get_name_():
    assert isinstance(get_name_(), str)


@pytest.mark.parametrize(
    ["cache"],
    [
        [True],
        [False],
    ],
)
def test_host_get_name(cache: str):
    assert isinstance(get_name(cache), str)


def test_host_get_seed_filename():
    assert isinstance(get_seed_filename(), str)


def test_signature():
    assert isinstance(signature(), list)


def test_tensor_processing_signature():
    assert isinstance(tensor_processing_signature(), list)

from abcli.tests import test_env
from blue_options import env


def test_abcli_env():
    test_env.test_abcli_env()


def test_blue_options_env():
    assert env.BLUE_PLUGIN_SECRET
    assert env.BLUE_PLUGIN_CONFIG



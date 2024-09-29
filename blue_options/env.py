from typing import Union
import os
from dotenv import load_dotenv
import pkg_resources


def load_config(
    package_name: str,
    verbose: bool = False,
):
    env_filename = pkg_resources.resource_filename(
        package_name,
        "config.env",
    )

    if verbose:
        print(f"loading {env_filename}.")

    assert load_dotenv(env_filename), pkg_resources.resource_listdir(package_name, "")


def load_env(
    package_name: str,
    verbose: bool = False,
):
    env_filename = os.path.join(
        os.path.dirname(
            pkg_resources.resource_filename(
                package_name,
                "",
            )
        ),
        ".env",
    )

    if verbose:
        print(f"loading {env_filename}.")

    load_dotenv(env_filename)


ABCUL = " \\\n\t"


abcli_log_filename = os.getenv(
    "abcli_log_filename",
    "",
)


CYAN = "\033[36m"
GREEN = "\033[32m"
LIGHTBLUE = "\033[96m"
NC = "\033[0m"
RED = "\033[31m"

EOP = "\033[33m"

HOST_NAME: Union[None, str] = None

abcli_hostname = os.getenv("abcli_hostname", "")

abcli_wifi_ssid = os.getenv("abcli_wifi_ssid", "")

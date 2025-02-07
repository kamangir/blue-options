from typing import Any
import os
from dotenv import load_dotenv
import pkg_resources


def get_env(name: str, default: Any = "") -> Any:
    output = os.getenv(
        name,
        default,
    )

    if isinstance(default, bool):
        return output == "1"

    # order is critical
    for output_type in [int, float]:
        if isinstance(default, output_type):
            try:
                return output_type(output)
            except:
                return default

    return output


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

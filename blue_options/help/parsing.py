import os
from typing import List

list_of_modules: List[str] = ["abcli"] + [
    item
    for item in os.getenv(
        "BLUE_OPTIONS_HELP_MODULE_LIST",
        "",
    ).split("+")
    if item
]


def get_callable_module(callable: str) -> str:
    for module in list_of_modules:
        if callable.startswith(module):
            return module

    return callable


def get_callable_suffix(callable: str) -> str:
    module = get_callable_module(callable)

    suffix = callable.split(module)[1]

    if suffix.startswith("_"):
        suffix = suffix[1:]

    return suffix

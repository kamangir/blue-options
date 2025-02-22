import os
from typing import List

list_of_modules: List[str] = [
    "abcli",
    "blue_assistant",
    "blue_flie",
    "blue_options",
    "blue_objects",
    "blue_geo",
    "blue_sbc",
    "blueflow",
    "blue_sandbox",
    "giza",
    "notebooks_and_scripts",
    "openai_commands",
    "roofai",
    "palisades",
] + [
    item
    for item in os.getenv(
        "BLUE_OPTIONS_HELP_MODULE_LIST",
        "",
    ).split("+")
    if item
]


def get_callable_module(
    callable: str,
    module_name_check: bool = True,
) -> str:
    for module in list_of_modules:
        if callable.startswith(module):
            return (
                os.getenv(f"{module}_module_name", module)
                if module_name_check
                else module
            )

    return callable


def get_callable_suffix(callable: str) -> str:
    module = get_callable_module(
        callable,
        module_name_check=False,
    )

    suffix = callable.split(module)[1]

    if suffix.startswith("_"):
        suffix = suffix[1:]

    return suffix

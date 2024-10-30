from typing import Dict

list_of_modules: Dict[str, Dict] = {
    "abcli": {},
}


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

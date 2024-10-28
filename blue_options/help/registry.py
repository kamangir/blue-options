from typing import Dict

list_of_modules: Dict[str, Dict] = {
    "abcli": {},
}


def get_module_name(callable: str) -> str:
    for module in list_of_modules.keys():
        if callable.startswith(module):
            return module

    return callable

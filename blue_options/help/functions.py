from typing import List, Dict, Callable, Union


def get_help(
    tokens: List[str],
    help_functions: Union[Callable, Dict[str, Union[Callable, Dict]]],
    mono: bool,
) -> str:
    if callable(help_functions) and not tokens:
        return help_functions(tokens, mono=mono)

    if not tokens:
        thing = help_functions
    elif tokens[0] in help_functions:
        return get_help(
            tokens[1:],
            help_functions[tokens[0]],
            mono=mono,
        )
    else:
        return ""

    if isinstance(thing, dict):
        return "\n".join(
            [
                get_help(
                    tokens[1:],
                    item,
                    mono=mono,
                )
                for item in thing.values()
            ]
        )

    assert callable(thing)
    return thing(tokens[1:], mono=mono)

import argparse
from typing import List, Dict, Callable, Union

from blueness.argparse.generic import sys_exit

from blue_options.logger import logger


def get_help(
    tokens: List[str],
    help_functions: Union[Callable, Dict[str, Union[Callable, Dict]]],
    mono: bool,
) -> str:
    if callable(help_functions):
        return help_functions(tokens, mono=mono)

    if not [token for token in tokens if token]:
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

    assert callable(thing), type(thing)
    return thing(tokens[1:], mono=mono)


def help_main(
    NAME: str,
    help_functions: Union[Callable, Dict[str, Union[Callable, Dict]]],
):
    parser = argparse.ArgumentParser(NAME)
    parser.add_argument(
        "--command",
        type=str,
    )
    parser.add_argument(
        "--mono",
        type=int,
        default=0,
        help="0|1",
    )
    args = parser.parse_args()

    content = get_help(
        tokens=args.command.strip().split(" "),
        help_functions=help_functions,
        mono=args.mono == 1,
    )

    if content:
        print(content)
    else:
        logger.warning(f'"{args.command}": help not found.')

    sys_exit(None, NAME, "help", bool(content))

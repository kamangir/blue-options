from functools import reduce
from typing import List, Dict, Tuple

from blue_options import env


def error(
    message: str,
    mono: bool = False,
) -> str:
    RED = "" if mono else env.RED
    NC = "" if mono else env.NC

    return f"❗️ {RED}{message}{NC}\n"


def hr(
    width: int,
    pattern: str,
    mono: bool = False,
) -> str:
    CYAN = "" if mono else env.CYAN
    NC = "" if mono else env.NC

    return "{}{}{}".format(
        CYAN,
        ((width // len(pattern) + 1) * pattern)[:width],
        NC,
    )


def show_usage(
    command: str,
    description: str,
    details: Dict[str, List[str]] = {},
    mono: bool = False,
) -> str:
    RED = "" if mono else env.RED
    NC = "" if mono else env.NC
    LIGHTBLUE = "" if mono else env.LIGHTBLUE
    CYAN = "" if mono else env.CYAN

    return "\n".join(
        [
            f"{LIGHTBLUE}{command}{NC}",
            f"{CYAN} . {description}{NC}",
        ]
        + reduce(
            lambda x, y: x + y,
            [
                (
                    [f"{CYAN}   {detail}{NC}"]
                    + (
                        [
                            f"{CYAN}      {item}{NC}"
                            for item in (
                                list_of_items
                                if isinstance(list_of_items, list)
                                else [list_of_items]
                            )
                        ]
                        if list_of_items
                        else []
                    )
                )
                for detail, list_of_items in details.items()
            ],
            [],
        )
    )
import os

NAME = "blue_options"

ICON = "🌀"

DESCRIPTION = f"{ICON} options for Bash."

VERSION = "4.80.1"

REPO_NAME = "blue-options"

MARQUEE = "https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true"


def fullname() -> str:
    abcli_git_branch = os.getenv("abcli_git_branch", "")
    return "{}-{}{}".format(
        NAME,
        VERSION,
        f"-abcli-{abcli_git_branch}" if abcli_git_branch else "",
    )

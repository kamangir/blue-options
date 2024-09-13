import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_options import NAME
from blue_options.host import get_name
from blue_options.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    default="get",
    help="get",
)
parser.add_argument(
    "--keyword",
    type=str,
    help="name",
)
args = parser.parse_args()


success = False
# bash-tested in test_abcli_host in blue-objects.
if args.task == "get":
    success = True
    output = f"unknown-{args.keyword}"

    if args.keyword == "name":
        output = get_name()

    print(output)
else:
    success = None


sys_exit(logger, NAME, args.task, success, log=False)

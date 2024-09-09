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
if args.task == "get":
    if args.keyword == "name":
        print(get_name())
        success = True
else:
    success = None


sys_exit(logger, NAME, args.task, success, log=args.log)

import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_options import NAME
from blue_options.help.registry import get_module_name
from blue_options.logger import logger

NAME = module.name(__file__, NAME)

list_of_tasks = ["get_module"]

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help=" | ".join(list_of_tasks),
)
parser.add_argument(
    "--callable",
    type=str,
)
args = parser.parse_args()

success = args.task in list_of_tasks
if args.task == "get_module":
    print(get_module_name(args.callable))
else:
    success = None

sys_exit(logger, NAME, args.task, success)

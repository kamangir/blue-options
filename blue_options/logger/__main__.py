import argparse
from blueness import module
from blueness.argparse.generic import sys_exit
from blue_options import NAME
from blue_options.env import CYAN, NC
from blue_options.logger.config import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    default="",
    help="hr",
)
parser.add_argument(
    "--width",
    type=int,
    default=80,
)
parser.add_argument(
    "--pattern",
    type=str,
    default=". .. ... .. ",
)
args = parser.parse_args()


success = False
if args.task == "hr":
    success = True
    print(
        "{}{}{}".format(
            CYAN,
            ((args.width // len(args.pattern) + 1) * args.pattern)[: args.width],
            NC,
        )
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)

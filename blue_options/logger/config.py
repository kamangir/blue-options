import logging
from logging import Logger
from logging.handlers import RotatingFileHandler
from blue_options.env import abcli_log_filename

# to hide "botocore.credentials Found credentials in environment variables."
logging.getLogger("botocore.credentials").setLevel(logging.WARNING)


# Based on https://stackoverflow.com/a/22313803
logging.addLevelName(logging.INFO, "")
logging.addLevelName(logging.DEBUG, "❓ ")
logging.addLevelName(logging.ERROR, "❗️ ")
logging.addLevelName(logging.WARNING, "⚠️  ")

logging_level = logging.INFO

logging.getLogger().setLevel(logging_level)

log_formatter = logging.Formatter("%(levelname)s%(name)s %(message)s")
try:
    file_handler = RotatingFileHandler(
        abcli_log_filename,
        maxBytes=10485760,
        backupCount=10000,
    )
    file_handler.setLevel(logging_level)
    file_handler.setFormatter(log_formatter)
    logging.getLogger().addHandler(file_handler)
except:
    pass

console_handler = logging.StreamHandler()
console_handler.setLevel(logging_level)
console_handler.setFormatter(log_formatter)
logging.getLogger().addHandler(console_handler)


def get_logger(ICON) -> Logger:
    return logging.getLogger(f"{ICON} ")


logger = get_logger("::")


# https://stackoverflow.com/a/10645855
def crash_report(description):
    logger.error(f"crash: {description}", exc_info=1)

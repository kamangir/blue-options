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


def log_long_text(
    logger: Logger,
    text: str,
    max_length: int = 100,
):
    logger.info(
        "{:,} char(s): {}{}".format(
            len(text),
            text[:max_length],
            "..." if len(text) > max_length else "",
        )
    )


def log_dict(
    logger: Logger,
    dict_of_items: dict,
    item_name_plural: str = "item(s)",
    max_count: int = 10,
    max_length: int = 100,
):
    logger.info(f"{len(dict_of_items)} {item_name_plural}")

    for index, (item, info) in enumerate(dict_of_items.items()):
        logger.info(
            "#{: 4} - {}: {}{}".format(
                index,
                item,
                info[:max_length],
                "..." if len(info) > max_length else "",
            )
        )

        if index > max_count:
            logger.info("...")
            break


def log_list(
    logger: Logger,
    list_of_items: list,
    item_name_plural: str = "item(s)",
    max_count: int = 10,
    max_length: int = 100,
):
    logger.info(f"{len(list_of_items)} {item_name_plural}")

    for index, item in enumerate(list_of_items):
        logger.info(
            "#{: 4} - {}{}".format(
                index,
                item[:max_length],
                "..." if len(item) > max_length else "",
            )
        )

        if index > max_count:
            logger.info("...")
            break

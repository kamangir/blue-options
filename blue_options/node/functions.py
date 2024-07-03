from blue_options.logger import logger


def func(arg: str) -> bool:
    logger.info(f"arg:{arg}")
    return True



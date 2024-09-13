from blue_options.logger import crash_report, get_logger, logger


def test_crash_report():
    crash_report("testing")


def test_get_logger():
    logger = get_logger("testing")
    assert logger is not None

    logger.info("testing")


def test_logger():
    logger.info("testing")

import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def _write_log(filename: str, level: str, message: str):
    log_file = LOG_DIR / filename

    logger = logging.getLogger(filename)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(log_file)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    if level == "info":
        logger.info(message)

    elif level == "error":
        logger.error(message)


def log_creation(message):
    _write_log(
        "ad_creation.log",
        "info",
        message
    )


def log_rollback(message):
    _write_log(
        "rollback.log",
        "info",
        message
    )


def log_validation(message):
    _write_log(
        "validation.log",
        "info",
        message
    )


def log_error(message):
    _write_log(
        "error.log",
        "error",
        message
    )
    

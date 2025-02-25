"""Logging functions for preprocessing."""
import logging
from logging import Logger
from pathlib import Path


def setup_logger(log_file_path: Path, level: str) -> Logger:
    """Create loggers in each method.

    Args:
        log_file_path (Path): Path of log
        level (str): Log level

    Returns:
        Logger: Logger of standard format for the project
    """
    if level == "info":
        logging_level = logging.INFO
    elif level == 'warning':
        logging_level = logging.WARNING
    elif level == 'debug':
        logging_level = logging.DEBUG
    elif level == 'error':
        logging_level = logging.ERROR
    elif level == 'critical':
        logging_level = logging.CRITICAL
    else:
        raise ValueError(
            'Level must be set as one of: info, warning, debug, error, critical'
        )

    typical_format = logging.Formatter(
        fmt='%(levelname)s - %(name)s - %(funcName)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger()
    output = logging.FileHandler(
        filename=log_file_path,
        mode='w'
    )
    logger.handlers = []
    output.setFormatter(typical_format)
    logger.addHandler(output)
    logger.setLevel(logging_level)

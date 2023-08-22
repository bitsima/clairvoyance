"""
Configure the basic settings of the logger, such as: file name, logging level and format.

Functions:
setup_logging() -> logging.Logger
"""

import logging


def setup_logging() -> logging.Logger:
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    return logging.getLogger(__name__)

"""Module for simple helper methods with no dependencies within the package"""

from functools import cache
from importlib.metadata import version as _version
from logging import BASIC_FORMAT, Formatter, StreamHandler, getLogger


@cache
def package() -> str:
    """Get the name of the top-level package"""
    return __name__.split(".")[0]


@cache
def version() -> str:
    """Get the version of the top-level package"""
    return _version(package())


def create_basic_logger(name: str, log_level: str) -> None:
    logger = getLogger(name)

    handler = StreamHandler()
    handler.setFormatter(Formatter(fmt=BASIC_FORMAT))
    logger.addHandler(handler)

    logger.setLevel(log_level)

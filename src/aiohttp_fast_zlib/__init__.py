"""Fast zlib module for aiohttp."""

__version__ = "0.1.1"

import importlib
import logging
import zlib as zlib_original
from typing import TYPE_CHECKING

import aiohttp

_LOGGER = logging.getLogger(__name__)

_AIOHTTP_SPLIT_VERSION = aiohttp.__version__.split(".")
_AIOHTTP_VERSION = (int(_AIOHTTP_SPLIT_VERSION[0]), int(_AIOHTTP_SPLIT_VERSION[1]))

if TYPE_CHECKING:
    best_zlib = zlib_original

try:
    from isal import isal_zlib as best_zlib  # type: ignore
except ImportError:
    try:
        from zlib_ng import zlib_ng as best_zlib  # type: ignore
    except ImportError:
        best_zlib = zlib_original

TARGETS = [
    "compression_utils",
    "http_writer",
    "http_writer",
    "http_parser",
    "multipart",
    "web_response",
]

if _AIOHTTP_VERSION >= (3, 11):
    TARGETS.append("_websocket.writer")
else:
    TARGETS.append("http_websocket")


def enable() -> None:
    """Enable fast zlib."""
    if best_zlib is zlib_original:
        _LOGGER.warning(
            "zlib_ng and isal are not available, falling back to zlib"
            ", performance will be degraded."
        )
        return
    for location in TARGETS:
        try:
            importlib.import_module(f"aiohttp.{location}")
        except ImportError:
            continue
        if module := getattr(aiohttp, location, None):
            module.zlib = best_zlib


def disable() -> None:
    """Disable fast zlib and restore the original zlib."""
    for location in TARGETS:
        if module := getattr(aiohttp, location, None):
            module.zlib = zlib_original

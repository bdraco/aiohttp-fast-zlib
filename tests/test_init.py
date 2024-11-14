import zlib as zlib_original
from unittest.mock import patch

import aiohttp.http_websocket
import pytest

import aiohttp_fast_zlib

try:
    from isal import (
        isal_zlib as expected_zlib,
    )
except ImportError:
    from zlib_ng import zlib_ng as expected_zlib


@pytest.mark.skipif(
    aiohttp_fast_zlib._AIOHTTP_VERSION >= (3, 11),
    reason="Only works with aiohttp less than 3.11+",
)
def test_enable_disable():
    """Test enable/disable."""
    assert aiohttp.http_websocket.zlib is zlib_original
    aiohttp_fast_zlib.enable()
    assert aiohttp.http_websocket.zlib is expected_zlib
    aiohttp_fast_zlib.disable()
    assert aiohttp.http_websocket.zlib is zlib_original
    aiohttp_fast_zlib.enable()
    assert aiohttp.http_websocket.zlib is expected_zlib
    aiohttp_fast_zlib.disable()


@pytest.mark.skipif(
    aiohttp_fast_zlib._AIOHTTP_VERSION < (3, 11),
    reason="Only works with aiohttp >= 3.11",
)
def test_enable_disable_greater_than_311():
    """Test enable/disable."""
    from aiohttp._websocket import writer

    assert writer.zlib is zlib_original
    aiohttp_fast_zlib.enable()
    assert writer.zlib is expected_zlib
    aiohttp_fast_zlib.disable()
    assert writer.zlib is zlib_original
    aiohttp_fast_zlib.enable()
    assert writer.zlib is expected_zlib
    aiohttp_fast_zlib.disable()


def test_enable_disable_when_all_missing():
    """Test enable/disable."""
    with patch.object(aiohttp_fast_zlib, "best_zlib", zlib_original):
        assert aiohttp.http_websocket.zlib is zlib_original
        aiohttp_fast_zlib.enable()
        assert aiohttp.http_websocket.zlib is zlib_original
        aiohttp_fast_zlib.disable()
        assert aiohttp.http_websocket.zlib is zlib_original
        aiohttp_fast_zlib.enable()
        assert aiohttp.http_websocket.zlib is zlib_original
        aiohttp_fast_zlib.disable()
        assert aiohttp.http_websocket.zlib is zlib_original

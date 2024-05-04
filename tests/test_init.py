import zlib as zlib_original
from unittest.mock import patch

import aiohttp.http_websocket

import aiohttp_fast_zlib

try:
    from isal import (
        isal_zlib as expected_zlib,
    )
except ImportError:
    from zlib_ng import zlib_ng as expected_zlib


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

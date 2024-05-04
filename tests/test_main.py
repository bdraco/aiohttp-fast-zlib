from aiohttp_fast_zlib.main import add


def test_add():
    """Adding two number works as expected."""
    assert add(1, 1) == 2

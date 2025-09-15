from redis import StrictRedis

import sandbox


def test_module() -> None:
    assert sandbox.check_integrity()


def test_redis() -> None:
    red = StrictRedis(decode_responses=True)
    red.set("foo", "bar")
    assert red.get("foo") == "bar"

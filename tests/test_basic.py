import sandbox


def test_integrity() -> None:
    assert sandbox.check_integrity()


def test_redis() -> None:
    from redis import StrictRedis

    red = StrictRedis(decode_responses=True)
    red.set("foo", "bar")
    assert red.get("foo") == "bar"

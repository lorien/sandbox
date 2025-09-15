import sandbox


def test_integrity() -> None:
    assert sandbox.check_integrity()


def test_redis() -> None:
    from redis import StrictRedis

    red = StrictRedis(decode_responses=True)
    red.set("foo", "bar")
    assert red.get("foo") == "bar"


def test_mysql() -> None:
    from MySQLdb import connect

    conn = connect(user="root", passwd="", db="grab_test")
    cur = conn.cursor()
    cur.execute("SHOW TABLES")
    print("Tables:")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

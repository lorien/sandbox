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

    conn = connect(host="127.0.0.1", port=3306, user="root", passwd="", db="grab_test")
    cur = conn.cursor()
    cur.execute("SHOW TABLES")
    print("Tables:")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()


def test_postgres() -> None:
    import psycopg2

    conn = psycopg2.connect(
        host="127.0.0.1",
        port=5432,
        dbname="grab_test",
    )

    cur = conn.cursor()
    cur.execute("SELECT tablename FROM pg_tables WHERE schemaname='public';")

    for row in cur.fetchall():
        print(row[0])

    cur.close()
    conn.close()

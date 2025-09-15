import sandbox


def test_integrity():
    assert sandbox.check_integrity()


def test_redis():
    from redis import StrictRedis

    red = StrictRedis(decode_responses=True)
    red.set("foo", "bar")
    assert red.get("foo") == "bar"


def test_mysql():
    from MySQLdb import connect

    conn = connect(
        db="grab_test",
        host="127.0.0.1",
        passwd="",
        port=3306,
        user="root",
    )
    cur = conn.cursor()
    cur.execute("SHOW TABLES")
    print("Tables:")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()


def test_postgres():
    import psycopg2

    conn = psycopg2.connect(
        dbname="grab_test",
        host="127.0.0.1",
        password="github",
        port=5432,
        user="github",
    )

    cur = conn.cursor()
    cur.execute("SELECT tablename FROM pg_tables WHERE schemaname='public';")

    for row in cur.fetchall():
        print(row[0])

    cur.close()
    conn.close()


def test_mongodb():
    from pymongo import MongoClient

    conn = MongoClient()

    for item in conn["grab_test"].list_collections():
        print(item)

    conn.close()

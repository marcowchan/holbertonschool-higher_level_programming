#!/usr/bin/python3
"""Lists all states."""
import MySQLdb
import sys


def main():
    """Connects to the database and lists all states."""
    options = {
        "host": "localhost",
        "port": 3306,
        "user": sys.argv[1],
        "passwd": sys.argv[2],
        "db": sys.argv[3],
        "charset": "utf8"
    }
    conn = MySQLdb.connect(**options)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

if (__name__ == "__main__"):
    main()

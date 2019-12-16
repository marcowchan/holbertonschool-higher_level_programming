#!/usr/bin/python3
"""Displays states matching the cli argument."""
import MySQLdb
import sys


def main():
    """Connects to the database and selects the matching states."""
    options = {
        "host": "localhost",
        "port": 3306,
        "user": sys.argv[1],
        "passwd": sys.argv[2],
        "db": sys.argv[3],
        "charset": "utf8"
    }
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id"
    conn = MySQLdb.connect(**options)
    cur = conn.cursor()
    cur.execute(query.format(sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

if (__name__ == "__main__"):
    main()

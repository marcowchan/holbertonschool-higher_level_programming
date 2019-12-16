#!/usr/bin/python3
"""Displays all cities."""
import MySQLdb
import sys


def main():
    """Connects to the database and displays all cities."""
    options = {
        "host": "localhost",
        "port": 3306,
        "user": sys.argv[1],
        "passwd": sys.argv[2],
        "db": sys.argv[3],
        "charset": "utf8"
    }
    query = "SELECT cities.id, cities.name, states.name FROM cities, states "
    query += "WHERE cities.state_id = states.id ORDER BY id"
    conn = MySQLdb.connect(**options)
    cur = conn.cursor()
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

if (__name__ == "__main__"):
    main()

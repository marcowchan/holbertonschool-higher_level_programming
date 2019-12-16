#!/usr/bin/python3
"""Displays all cities from a state."""
import MySQLdb
import sys


def main():
    """Connects to the database and displays all cities from a state."""
    options = {
        "host": "localhost",
        "port": 3306,
        "user": sys.argv[1],
        "passwd": sys.argv[2],
        "db": sys.argv[3],
        "charset": "utf8"
    }
    query = "SELECT cities.name FROM cities INNER JOIN states "
    query += "ON cities.state_id = states.id AND states.name = %s "
    query += "ORDER BY cities.id"
    conn = MySQLdb.connect(**options)
    cur = conn.cursor()
    cur.execute(query, (sys.argv[4],))
    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    conn.close()

if (__name__ == "__main__"):
    main()

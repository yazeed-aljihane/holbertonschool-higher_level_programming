#!/usr/bin/python3
"""
This script lists all states with a name starting with N (upper case)
from the database hbtn_0e_0_usa.

The script takes 3 arguments: mysql username, mysql password and database name.
"""
import MySQLdb
import sys


def list_all_state():
    """Connects to the database and prints states starting with N.

    Args:
        None (Uses sys.argv for input).

    Returns:
        None.
    """
    if len(sys.argv) != 4:
        return

    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cur = db.cursor()

        cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                     ORDER BY id ASC")

        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        db.close()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    list_all_state()

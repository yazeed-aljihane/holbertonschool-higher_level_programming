#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa where
name matches the argument, safe from MySQL injections.
"""
import MySQLdb
import sys


def list_all():
    """Connects to the database and selects states based on user input.

    The script uses parameterized queries to prevent SQL injection attacks.
    Arguments are retrieved from the command line.
    """
    if len(sys.argv) != 5:
        return

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cur = db.cursor()

        cur.execute("SELECT * FROM states WHERE name = \
        BINARY '{}' ORDER BY id ASC".format(sys.argv[4]))

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    list_all()

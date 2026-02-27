#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
It uses JOIN to display the state name along with city data.
"""
import MySQLdb
import sys


def list_all():
    """Connects to the database and selects cities with their states.

    The query joins 'cities' and 'states' tables on state_id.
    Results are sorted by city ID in ascending order.
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

        query = "SELECT cities.id, cities.name, states.name " \
                "FROM cities INNER JOIN states ON " \
                "cities.state_id = states.id ORDER BY cities.id ASC"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    list_all()

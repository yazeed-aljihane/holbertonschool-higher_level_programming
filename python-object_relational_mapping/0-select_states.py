#!/usr/bin/env python3
"""
This script lists all states from the database hbtn_0e_0_usa.

The script takes 3 arguments: mysql username, mysql password and database name.
It connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys


def list_states():
    """Connects to the database and prints all states.

    This function retrieves all records from the 'states' table of the
    specified database and prints them to the standard output.

    Args:
        username (str): The MySQL username provided as the first argument.
        password (str): The MySQL password provided as the second argument.
        db_name (str): The database name provided as the third argument.

    Returns:
        None
    """
    # Accessing command line arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    try:
        # Establish connection to the MySQL server
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=passwd,
            db=db
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Execute the SQL command to fetch all states ordered by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows from the executed query
        query_rows = cursor.fetchall()

        # Display the results
        for row in query_rows:
            print(row)

        # Close the cursor and the connection
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    """
    Prevents the script from being executed when imported.
    Only runs when called directly.
    """
    if len(sys.argv) == 4:
        list_states()

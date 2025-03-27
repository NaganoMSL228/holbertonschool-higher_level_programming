#!/usr/bin/python3
"""Script that lists all states with name starting with N from database"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    List all states with name starting with N from database.
    Takes 3 arguments:
        mysql username (str)
        mysql password (str)
        database name (str)
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor object
    cursor = db.cursor()

    # Execute query with LIKE clause to filter states starting with N
    cursor.execute("""SELECT * FROM states
                     WHERE BINARY name LIKE 'N%'
                     ORDER BY id ASC""")

    # Fetch all rows
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()

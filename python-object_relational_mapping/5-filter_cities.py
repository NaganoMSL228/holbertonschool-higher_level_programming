#!/usr/bin/python3
"""Script that lists all cities of a given state"""

import MySQLdb
import sys

if __name__ == "__main__":
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

    # Execute query with safe parameter binding
    query = """SELECT cities.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""
    cursor.execute(query, (sys.argv[4],))

    # Fetch results and format as comma-separated string
    print(", ".join([row[0] for row in cursor.fetchall()]))

    # Close cursor and connection
    cursor.close()
    db.close()

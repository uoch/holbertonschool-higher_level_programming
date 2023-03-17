#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == '__main__':
    # Retrieve command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=db_name)

    # Create cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query to retrieve all cities from database and sort by id
    cursor.execute("SELECT * FROM cities ORDER BY cities.id ASC")

    # Fetch all rows returned by query
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
    
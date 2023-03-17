#!/usr/bin/python3
"""Script that displays all values in the states table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
import sys

if __name__ == '__main__':
    # Retrieve command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=db_name)

    # Create cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query to retrieve all states where name matches the argument
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch all rows returned by query
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

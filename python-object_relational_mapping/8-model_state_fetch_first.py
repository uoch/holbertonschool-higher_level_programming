#!/usr/bin/python3
"""Write a script that prints the first State object
from the database hbtn_0e_6_usa"""
import sqlalchemy
import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states LIMIT 1")

    result = cur.fetchone()

    if result:
        print(f"{result[0]}: {result[1]}")
    else:
        print("Nothing")

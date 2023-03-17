#!/usr/bin/python3

"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys
if __name__ == "__main__":

    user = sys.argv[1]
    pas = sys.argv[2]
    data = sys.argv[3]
    name = sys.argv[4]

    connection = MySQLdb.connect(
        host='localhost', port=3306, database=data, user=user, password=pas)
    record = connection.cursor()
    record2 = connection.cursor()
    record.execute("SELECT * FROM cities JOIN states ORDER BY cities.id ASC")

    records = record.fetchall()
    m = [i[2] for i in records if i[4] == name and i[1] == i[3]]
    if not m:
        print()
    else:
        print(", ".join(str(a) for a in m))

#!/usr/bin/python3


"""
IN this script we learn how to filter name
"""


import MySQLdb
import sys

def filter_states(username, password, database):
    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                )
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE BINARY name LIKE 'N%'"
        cursor.execute(query)
        result = cursor.fetchall()
        for i in result:
            print(i)
    except MySQLdb as e:
        print(f"error:{e}")

    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    filter_states(username, password, database)

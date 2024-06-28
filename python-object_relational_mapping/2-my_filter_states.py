#!/usr/bin/python3

"""
In this script we learn how to search a name with a argument
"""

import MySQLdb
import sys

def search_specific_state(username, password, database, state_name):
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE BINARY name LIKE\
                '{}';".format(state_name)
        cursor.execute(query)
        result = cursor.fetchall()
        for i in result:
            print(i)
    except MySQLdb as e:
        print(f"error: {e}")

    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    search_specific_state(username, password, database, state_name)


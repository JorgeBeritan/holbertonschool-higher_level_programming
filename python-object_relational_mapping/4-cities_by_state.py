#!/usr/bin/python3


"""
In this script we learn how to use inner join with query
on MySQLbd
"""



import MySQLdb
import sys

def cities_state(username, password, database):
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

        cursor = db.cursor()
        query = "SELECT cities.id, cities.name, states.name FROM \
                cities INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC"

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

    cities_state(username, password, database);

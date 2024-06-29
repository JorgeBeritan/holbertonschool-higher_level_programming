#!/usr/bin/python3


"""
In this script we list all cities from a specific state
"""

import MySQLdb
import sys

def list_cities(username, password, database, state_name):
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
        cursor = db.cursor()
        query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
        """
        cursor.execute(query, (state_name,))
        result = cursor.fetchall()
        
        print(", ".join([city[0] for city in result]))

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

    list_cities(username, password, database, state_name)




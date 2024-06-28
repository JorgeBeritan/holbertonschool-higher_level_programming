#!/usr/bin/python3

import MySQLdb
import sys

def safe_state(username, password, database, search_state):
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
        cursor = db.cursor()
        query = ("SELECT * FROM states WHERE BINARY name LIKE %s" +
                 "ORDER BY states.id")    
        cursor.execute(query, (search_state,))
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
    search_state = sys.argv[4]

    safe_state(username, password, database, search_state)

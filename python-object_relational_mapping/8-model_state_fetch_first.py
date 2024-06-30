#!/usr/bin/python3


"""
In this script we learn how to fitler information
In this script we learn how to fitler information
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

def list_id(username, password, database):
    dburl = ('mysql+mysqldb://{}:{}@localhost/{}'
          .format(username, password, database))

    engine = create_engine(dburl)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id).first()

    if query is not None:
        print("{}: {}".format(query.id, query.name))
    else:
        print("Nothing")
    session.close()
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_id(username, password, database)

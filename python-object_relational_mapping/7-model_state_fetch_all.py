#!/usr/bin/python3


"""
In this script we learn how to send query
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_state(username, password, database):
    dburl = 'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password,\
            database, pool_pre_ping=True)
    engine = create_engine(dburl)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for i in states:
        print("{}: {}".format(i.id, i.name))

    session.close()

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_state(username, password, database)

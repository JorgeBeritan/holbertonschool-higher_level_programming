#!/usr/bin/python3


"""
In this script we learn how inserte a table with sqlalchemy
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String


class State(Base):
    """
    In this clase we create state
    """
    __tablename__ = "states"

    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


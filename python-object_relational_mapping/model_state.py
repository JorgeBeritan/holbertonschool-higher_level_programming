#!/usr/bin/python3


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String


class State(Base):
    __tablename__ = "states"

    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


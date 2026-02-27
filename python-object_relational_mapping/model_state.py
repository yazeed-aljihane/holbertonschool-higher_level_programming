#!/usr/bin/python3
"""
This module defines a State class and an instance Base = declarative_base().
It maps the State class to the MySQL table 'states'.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.

    Attributes:
        id (int): The state's id (Primary Key, unique, auto-generated).
        name (str): The state's name (max 128 characters, not null).
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

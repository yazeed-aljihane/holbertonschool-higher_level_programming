#!/usr/bin/python3
"""
Contains the class definition of a City.
This module defines the City class which inherits from Base.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """Represents a city for a MySQL database.

    Attributes:
        id (int): The city's id (Primary Key).
        name (str): The city's name.
        state_id (int): The city's state id (Foreign Key to states.id).
    """
    __tablename__ = 'cities'

    id = Column(
         Integer,
         primary_key=True,
         nullable=False,
         autoincrement=True
     )
    name = Column(
        String(128),
        nullable=False
    )

    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )

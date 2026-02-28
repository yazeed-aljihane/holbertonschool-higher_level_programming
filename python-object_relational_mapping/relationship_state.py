#!/usr/bin/python3
"""
Contains the class definition of a State with relationship.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """Represents a state with a relationship to City.

    Attributes:
        id (int): State id.
        name (str): State name.
        cities (list): Relationship to City class with cascade delete.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete-orphan"
    )

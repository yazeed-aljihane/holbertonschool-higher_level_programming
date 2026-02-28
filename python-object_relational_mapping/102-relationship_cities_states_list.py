#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa.

This script uses the 'state' relationship to access the State object
linked to each City and displays them in a specific format.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def list_cities_with_states():
    """Fetches all cities and their linked states using one query.

    Results are sorted by City.id in ascending order.
    Format: <city id>: <city name> -> <state name>
    """
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities_with_states()

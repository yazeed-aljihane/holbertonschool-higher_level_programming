#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects from the database.

This script uses the relationship 'cities' to fetch data and displays it
in a specific format: <state id>: <state name> followed by indented cities.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def list_all_relationships():
    """Lists states and their cities from the database.

    Uses a single query and the relationship defined in State class.
    Results are sorted by State.id and City.id.
    """
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

        for city in sorted(state.cities, key=lambda x: x.id):
            print("\t{}: {}".format(city.id, city.name))

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_all_relationships()

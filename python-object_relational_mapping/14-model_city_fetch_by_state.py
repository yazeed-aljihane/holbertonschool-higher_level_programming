#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.

This script connects to a MySQL server and performs a join between
the states and cities tables to display information in a specific format.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state():
    """Fetches and prints cities with their corresponding state names.

    The results are ordered by City.id in ascending order.
    Format: <state name>: (<city id>) <city name>
    """
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query_results = session.query(State, City).filter(
        State.id == City.state_id
    ).order_by(City.id).all()

    for state, city in query_results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        fetch_cities_by_state()

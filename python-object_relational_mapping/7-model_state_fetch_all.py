#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
This script uses SQLAlchemy to fetch and display data.
"""
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_all_states():
    """Connects to the database and fetches all states.

    The results are sorted by State.id in ascending order and
    printed in the format 'id: name'.
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
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        fetch_all_states()

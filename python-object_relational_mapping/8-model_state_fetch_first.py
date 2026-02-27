#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
This script uses SQLAlchemy and handles empty tables gracefully.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_all():
    """Connects to the database and retrieves only the first state.

    The state is determined by the lowest ID. If no state exists,
    it prints 'Nothing'.
    """
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print('{}: {}'.format(first_state.id, first_state.name))
    else:
        print('Nothing')

    session.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        fetch_all()

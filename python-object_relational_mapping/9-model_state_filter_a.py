#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_a():
    """Connects to the database and filters states containing 'a'.

    The result is sorted by states.id in ascending order.
    """
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    for state in states:
        print('{}: {}'.format(state.id, state.name))

    session.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        list_a()

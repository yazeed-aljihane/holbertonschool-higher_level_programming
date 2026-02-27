#!/usr/bin/python3
"""
Adds the State object 'Louisiana' to the database hbtn_0e_6_usa.
This script prints the new state's id after saving it.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def insert_state():
    """Connects to the DB and inserts 'Louisiana' into the states table.
    """
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print("{}".format(new_state.id))

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        insert_state()

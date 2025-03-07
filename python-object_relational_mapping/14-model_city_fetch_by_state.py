#!/usr/bin/python3
"""Script that prints all City objects from database"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        )
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities joined with states
    cities = session.query(State, City).join(City).\
        order_by(City.id).all()

    # Display results
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

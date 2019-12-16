#!/usr/bin/python3
# List the first State object.
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).first()
    if (result):
        print("1: {}".format(result.name))
    else:
        print("Nothing")
    session.close()

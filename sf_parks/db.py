import os
import argparse
from sqlmodel import SQLModel, create_engine
# from .models import (
#     FilmLocations,
#     ParkScores,
#     PrivateOpenSpaces
# )

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}

def get_engine():
    return create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    engine = get_engine()
    SQLModel.metadata.create_all(engine)

def teardown_db():
    os.remove(sqlite_file_name)


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('command')
#     args = parser.parse_args()

#     if args.command == 'create':
#         create_db_and_tables()
#     elif args.command == 'destroy':
#         teardown_db()
#     else:
#         raise ValueError(f'Command passed to db.py must be one of `create` or `destroy` not {args.command}')

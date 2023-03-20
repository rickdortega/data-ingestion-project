import os
from sqlmodel import SQLModel, create_engine

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}

def get_engine():
    return create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    engine = get_engine()
    SQLModel.metadata.create_all(engine)

def teardown_db():
    try:
        os.remove(sqlite_file_name)
    except Exception as e:
        print(f'Error attempting to tear down database {sqlite_file_name}\nError: {e}')

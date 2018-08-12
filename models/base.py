from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from config import Config


Base = declarative_base()


def db_connect():
    return create_engine(Config.DATABASE_URL)


def create_tables(engine):
    Base.metadata.create_all(engine)

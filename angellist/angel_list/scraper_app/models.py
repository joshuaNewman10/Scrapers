from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import Column, Integer, String, DateTime

import settings

DeclarativeBase = declarative_base()

def db_connect():
  """
  Performs database connection using db settings in settings.py
  returns sqlalchemy engine instance
  """
  return create_engine(URL(**settings.DATABASE))

def create_companies_table(engine):
  """"""
  DeclarativeBase.metadata.create_all(engine)

class Companies(DeclarativeBase):
  """
  sqlalchemy companies model
  """
  __tablename__ = "companies"

  id = Column(Integer, primary_key=True)
  test = Column('test', String, nullable=True)

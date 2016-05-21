
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Metadata = Base.metadata

engine = create_engine('sqlite:///spark.sqlite')
factory = sessionmaker(bind=engine)
Session = scoped_session(factory)

from .model import *
Metadata.bind = engine
Metadata.create_all()



"""
database
========
"""

__all__ = ['Base', 'cleaning', 'models', 'initialize', 'processing',
           'terminate']

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from . import cleaning, models, processing


def __bool__(self):
    return any(
        not (column.primary_key or getattr(self, column.name) is None)
        for column in self.__mapper__.columns
    )


def __getitem__(self, name):
    return self.__mapper__.columns[name]


def __repr__(self):
    attributes = ((attribute, getattr(self, attribute))
                  for attribute in self.__class__.__mapper__.columns.keys())
    pairs = ('{}={}'.format(attribute, repr(value))
             for attribute, value in attributes if value is not None)
    return '{}({})'.format(self.__class__.__name__, ', '.join(pairs))


Base.__bool__ = __bool__
Base.__getitem__ = __getitem__
Base.__repr__ = Base.__str__ = __repr__


def initialize(url):
    engine = create_engine(url, convert_unicode=True)
    session = scoped_session(sessionmaker(bind=engine))
    Base.query = session.query_property()
    Base.metadata.create_all(bind=engine)
    return engine, session


def terminate(engine, session):
    session.close_all()
    engine.dispose()

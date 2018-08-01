#!/usr/bin/python3
"""
configuration file
"""


from models.base_model import BaseModel, Base
from models.user import User
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL


config = {'drivername': 'mysql+mysqldb',
            'username': os.getenv('HBNB_YELP_MYSQL_USER'),
            'password': os.getenv('HBNB_YELP_MYSQL_PWD'),
            'host': os.getenv('HBNB_YELP_MYSQL_HOST'),
            'database':  os.getenv('HBNB_YELP_MYSQL_DB')}
db_engine = create_engine(URL(**config))

dbengine = create_engine(
               'mysql+mysqldb://{}:{}@{}/{}'.format(
                    os.getenv('HBNB_YELP_MYSQL_USER'),
                    os.getenv('HBNB_YELP_MYSQL_PWD'),
                    os.getenv('HBNB_YELP_MYSQL_HOST'),
                    os.getenv('HBNB_YELP_MYSQL_DB')))

if os.getenv('HBNB_YELP_ENV') == 'test':
    Base.metadata.drop_all(bind=db_engine)
Base.metadata.create_all(db_engine)
db_session = scoped_session(sessionmaker(bind=db_engine,
                                         expire_on_commit=False))

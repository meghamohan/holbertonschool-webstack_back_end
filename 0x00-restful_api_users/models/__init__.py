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


db_engine = create_engine(
               'mysql+mysqldb://{}:{}@{}/{}'.format(
                    os.environ.get('HBNB_YELP_MYSQL_USER'),
                    os.environ.get('HBNB_YELP_MYSQL_PWD'),
                    os.environ.get('HBNB_YELP_MYSQL_HOST'),
                    os.environ.get('HBNB_YELP_MYSQL_DB')))

if os.getenv("HBNB_YELP_MYSQL_DB") == "hbtn_yelp_test":
    Base.metadata.drop_all(bind=db_engine)
Base.metadata.create_all(db_engine)
db_session = scoped_session(sessionmaker(bind=db_engine,
                                         expire_on_commit=False))

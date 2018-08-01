#!/usr/bin/python3
"""
base model class
"""
import uuid
from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class BaseModel:
    """
    base model class for other classes
    """
    id = Column(String(60), nullable=False, primary_key=True, \
                default=str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updates_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self):
        """ initializing basemodel """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

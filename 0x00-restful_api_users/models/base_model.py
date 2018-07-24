#!/usr/bin/python3
"""
base model class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    base model class for other classes
    """
    id = None
    created_at = None
    updates_at = None

    def __init__(self):
        """ initializing basemodel """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

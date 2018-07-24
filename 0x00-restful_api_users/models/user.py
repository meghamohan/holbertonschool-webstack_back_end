#!/usr/bin/python3
"""
user class
"""
from models.base_model import BaseModel
from sqlalchemy import Integer, String, Float, Column
from datetime import datetime
import uuid
import hashlib


class User(BaseModel):
    """ user class """
    email = None
    first_name = None
    last_name = None
    _password = None

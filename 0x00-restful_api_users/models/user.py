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

    def display_name(self):
        """ display user details """
        if self.email == self.first_name == self.last_name == None:
            return ''
        elif self.email is not None and (self.first_name == self.last_name == None):
            return self.email
        elif self.first_name is not None and self.last_name is None:
            return self.first_name
        elif self.first_name is None and self.last_name is not None:
            return self.last_name
        else:
            return self.first_name + ' ' + self.last_name

    @property
    def password(self):
        """ pwd getter """
        return self._password

    @password.setter
    def password(self, pwd):
        """ pwd getter """
        if pwd is None or type(pwd) is not str:
            self._password = None
        else:
            pwd = hashlib.md5(bytes(pwd, encoding='utf8')).hexdigest()
            self._password = pwd

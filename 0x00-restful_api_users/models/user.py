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

    def is_valid_password(self, pwd):
        """ to check if the pwd is valid or not """
        if type(pwd) is not str or self._password is None:
            return False
        pwd = hashlib.md5(bytes(pwd, encoding='utf8')).hexdigest()
        if pwd == self._password:
            return True
        else:
            return False

    def __str__(self):
        """ displays user instance  """
        retStr = "[{}] {} - {} - {}".format(
                            self.__class__.__name__,
                            self.id,
                            self.email,
                            self.display_name())
        return retStr

    def to_dict(self):
        """ returns a serialized user instance """
        dict1 = {}
        for key, val in self.__dict__.items():
            if key == 'updated_at' or key == 'created_at':
                dict1[key] = val.strftime('%Y-%m-%d %H:%M:%S')
            else:
                dict1[key] = str(val)
        return dict1

#!/usr/bin/python3
"""
testcases for base class
"""
from datetime import datetime
import unittest
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ testcases for basemodel class """
    def setUp(self):
        """ initialize """
        self.model = BaseModel()

    def testClass(self):
        """ test the base class instance"""
        self.assertIsInstance(self.model, BaseModel)

    def testClass2(self):
        """ test the base class instance"""
        self.assertIsNotNone(self.model)

    def testId(self):
        """ test id attribute """
        self.assertIsInstance(self.model.id, str)
        self.assertIsNotNone(self.model.id)

    def testCreatedAt(self):
        """ test created_at attribute """
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsNotNone(self.model.created_at)

    def testUpdatedAt(self):
        """ test updated_at attribute """
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertIsNotNone(self.model.updated_at)


if __name__ == '__main__':
    unittest.main()

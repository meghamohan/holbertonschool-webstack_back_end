#!/usr/bin/python3
"""
test cases for user class
"""
from models.user import User
import unittest
from datetime import datetime


class ModelTests(unittest.TestCase):
    """ testcases for userclass """
    def setUp(self):
        """ sets up the classes """
        self.model = User()

    def testClass(self):
        """ test the class """
        self.assertIsNotNone(self.model)
        self.assertIsInstance(self.model, User)

    def testId(self):
        """ test id attribute """
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.id, str)

    def testCreatedAt(self):
        """ test created at attribute """
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsNotNone(self.model.created_at)

    def testUpdatedAt(self):
        """ test updated at attribute """
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertIsNotNone(self.model.updated_at)

    def testFirstName(self):
        """ test updated at attribute """
        self.model.first_name = "megha"
        self.assertIsInstance(self.model.first_name, str)
        self.assertIsNotNone(self.model.first_name)
        self.assertEqual(self.model.first_name, "megha")

    def testFirstName(self):
        """ test updated at attribute """
        self.model.last_name = "megha"
        self.assertIsInstance(self.model.last_name, str)
        self.assertIsNotNone(self.model.last_name)
        self.assertEqual(self.model.last_name, "megha")

    def testEmail(self):
        """ test updated at attribute """
        self.model.email = "megha@mohan.com"
        self.assertIsInstance(self.model.email, str)
        self.assertIsNotNone(self.model.email)
        self.assertEqual(self.model.email, "megha@mohan.com")

    def testPwd(self):
        """ test password attribute """
        self.assertEqual(self.model.password, None)
        self.model.password = "asdfghjk"
        self.assertEqual(self.model.password, "bf709005906087dc1256bb4449d8774d")
        self.assertIsInstance(self.model.password, str)

    def testDsiplayName(self):
        """ test display name property """
        self.model.first_name = self.model.last_name = self.model.email = None
        self.assertEqual(self.model.display_name(), '')
        self.model.email = 'megha@mohan.com'
        self.assertEqual(self.model.display_name(), 'megha@mohan.com')
        self.model.first_name = 'megha'
        self.assertEqual(self.model.display_name(), 'megha')
        self.model.last_name = 'mohan'
        self.assertEqual(self.model.display_name(), 'megha mohan')


if __name__ == '__main__':
    unittest.main()

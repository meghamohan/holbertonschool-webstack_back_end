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

    def testIsValidFn(self):
        """test is_alid function"""
        self.model.password = "MeghaMohan"
        self.assertTrue(self.model.is_valid_password('MeghaMohan'))
        self.assertFalse(self.model.is_valid_password(29))
        self.assertFalse(self.model.is_valid_password(None))
        self.assertFalse(self.model.is_valid_password(['hi']))

    def testDsiplayName1(self):
        """ test display name property """
        self.model.first_name = self.model.last_name = self.model.email = None
        self.assertEqual(self.model.display_name(), '')
    def testDsiplayName2(self):
        """ test display name property """
        self.model.email = 'megha@mohan.com'
        self.assertEqual(self.model.display_name(), 'megha@mohan.com')
    def testDsiplayName3(self):
        """ test display name property """
        self.model.first_name = 'megha'
        self.assertEqual(self.model.display_name(), 'megha')
    def testDsiplayName4(self):
        """ test display name property """
        self.model.last_name = 'mohan'
        self.assertEqual(self.model.display_name(), 'mohan')
    def testDsiplayName5(self):
        """ test display name property """
        self.model.first_name = 'megha'
        self.model.email = 'megha@mohan.com'
        self.model.last_name = 'mohan'
        self.assertEqual(self.model.display_name(), 'megha mohan')

    def testToDict(self):
        """ test to_dict attribute """
        dateTime = "%Y-%m-%d %H:%M:%S"
        usrStr = {'id': self.model.id, 'email': 'megha@mohan.com',
                  'first_name': 'Megha',
                  'last_name': 'Mohan',
                  'created_at': self.model.created_at.strftime(dateTime),
                  'updated_at': self.model.created_at.strftime(dateTime)}
        self.model.email = "megha@mohan.com"
        self.model.first_name = "Megha"
        self.model.last_name = "Mohan"
        self.assertEqual(usrStr, self.model.to_dict())

    def testStr1(self):
        """ test str function """
        strResponse = '[User] ' + self.model.id + ' - None - '
        self.assertEqual(str(self.model), strResponse)
    def testStr2(self):
        """ test str function """
        self.model.email = 'megha@mohan.com'
        strResponse = '[User] ' + self.model.id + \
                        ' - megha@mohan.com - megha@mohan.com'
        self.assertEqual(str(self.model), strResponse)
    def testStr3(self):
        """ test str function """
        self.model.first_name = None
        self.model.last_name = 'Mohan'
        self.model.email = 'megha@mohan.com'
        strResponse = '[User] ' + self.model.id + \
                        ' - megha@mohan.com - Mohan'
        self.assertEqual(str(self.model), strResponse)
    def testStr3(self):
        """ test str function """
        self.model.first_name = 'Megha'
        self.model.last_name = None
        self.model.email = 'megha@mohan.com'
        strResponse = '[User] ' + self.model.id + \
                        ' - megha@mohan.com - Megha'
        self.assertEqual(str(self.model), strResponse)
    def testStr5(self):
        """ test str function """
        self.model.first_name = 'Megha'
        self.model.last_name = 'Mohan'
        self.model.email = 'megha@mohan.com'
        strResponse = '[User] ' + self.model.id + \
                        ' - megha@mohan.com - Megha Mohan'
        self.assertEqual(str(self.model), strResponse)
        
if __name__ == '__main__':
    unittest.main()

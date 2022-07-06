#!/usr/bin/python3
"""
Test model - User
"""

from models.base_model import BaseModel
from models.user import User
import unittest
import pep8


class TestUser(unittest.TestCase):
    """
    User test class
    """
    @classmethod
    def setUpClass(cls):
        """
        Setting up class attributes
        """
        cls.user = User()
        cls.user.email = "test@email.com"
        cls.user.password = "12345"
        cls.user.first_name = "Test"
        cls.user.last_name = "User"

    @classmethod
    def tearDownClass(cls):
        """
        Teardown at the end of the test
        """
        del cls.user

    def test_is_subclass(self):
        """
        Method that checks:
            if the subclass is set correctly
        """
        user = User()
        self.assertTrue(issubclass(user.__class__, BaseModel))

    def test_name_attr(self):
        """
        Method that checks:
            if the name of class is set correctly
        """
        user = User()
        self.assertEqual(user.__class__.__name__, "User")

    def test_to_dict_creates_dict(self):
        """
        Method that checks:
            if to_dict is set correctly
        """
        user = User()
        self.assertTrue(hasattr(user, 'to_dict') is True)
        am_dict = user.to_dict
        self.assertTrue(type(am_dict), dict)

    def test_types(self):
        """
        Method that checks:
            if attr types were set correctly
        """
        user = User()
        self.assertTrue(type(user.email) is str)
        self.assertTrue(type(user.password) is str)
        self.assertTrue(type(user.first_name) is str)
        self.assertTrue(type(user.last_name) is str)

    def test_pep8_conformance_file_storage(self):
        """
        Method that tests:
            if a file meet with pep8 criteria
        """
        style = pep8.StyleGuide()
        check = style.check_files(['models/user.py'])
        self.assertEqual(
            check.total_errors,
            0,
            'PEP8 style errors: %d' % check.total_errors
        )


if __name__ == "__main__":
    unittest.main()

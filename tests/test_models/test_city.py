#!/usr/bin/python3
"""
Test model - City
"""

from models.base_model import BaseModel
from models.city import City
import unittest
import pep8


class TestCity(unittest.TestCase):
    """
    City test class
    """

    @classmethod
    def setUpClass(cls):
        """
        Setting up class attributes
        """
        cls.city = City()
        cls.city.state_id = "1234"
        cls.city.name = "Test"

    @classmethod
    def tearDownClass(cls):
        """
        Teardown at the end of the test
        """
        del cls.city

    def test_is_subclass(self):
        """
        Method that checks:
            if the subclass is set correctly
        """
        city = City()
        self.assertTrue(issubclass(city.__class__, BaseModel))

    def test_name_attr(self):
        """
        Method that checks:
            if the name of class is set correctly
        """
        city = City()
        self.assertEqual(city.__class__.__name__, "City")

    def test_to_dict_creates_dict(self):
        """
        Method that checks:
            if to_dict is set correctly
        """
        city = City()
        self.assertTrue(hasattr(city, 'to_dict') is True)
        am_dict = city.to_dict
        self.assertTrue(type(am_dict), dict)

    def test_str(self):
        """
        Method that checks:
            if name and state is set correctly
        """
        city = City()
        self.assertTrue(type(city.name) is str)
        self.assertTrue(type(city.state_id) is str)

    def test_pep8_conformance_file_storage(self):
        """
        Method that tests:
            if a file meet with pep8 criteria
        """
        style = pep8.StyleGuide()
        check = style.check_files(['models/city.py'])
        self.assertEqual(
            check.total_errors,
            0,
            'PEP8 style errors: %d' % check.total_errors
        )


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""
Test model - Amenity
"""

from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
import pep8


class TestAmenity(unittest.TestCase):
    """
    Amenity test class
    """

    @classmethod
    def setUpClass(cls):
        """
        Setting up class attributes
        """
        cls.amenity = Amenity()
        cls.amenity.name = ""

    @classmethod
    def tearDownClass(cls):
        """
        Teardown at the end of the test
        """
        del cls.amenity

    def test_is_subclass(self):
        """
        Method that checks:
            if the subclass is set correctly
        """
        amenity = Amenity()
        self.assertTrue(issubclass(amenity.__class__, BaseModel))

    def test_name_attr(self):
        """
        Method that checks:
            if the name of class is set correctly
        """
        amenity = Amenity()
        self.assertEqual(amenity.__class__.__name__, "Amenity")

    def test_to_dict_creates_dict(self):
        """
        Method that checks:
            if to_dict is set correctly
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'to_dict') is True)
        am_dict = amenity.to_dict
        self.assertTrue(type(am_dict), dict)

    def test_str(self):
        """
        Method that checks:
            if name is set correctly
        """
        amenity = Amenity()
        self.assertTrue(type(amenity.name) is str)

    def test_pep8_conformance_file_storage(self):
        """
        Method that tests:
            if a file meet with pep8 criteria
        """
        style = pep8.StyleGuide()
        check = style.check_files(['models/amenity.py'])
        self.assertEqual(
            check.total_errors,
            0,
            'PEP8 style errors: %d' % check.total_errors
        )


if __name__ == "__main__":
    unittest.main()

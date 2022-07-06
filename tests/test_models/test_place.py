#!/usr/bin/python3
"""
Test model - Place
"""

from models.base_model import BaseModel
from models.place import Place
import unittest
import pep8


class TestPlace(unittest.TestCase):
    """
    Place test class
    """
    @classmethod
    def setUpClass(cls):
        """
        Setting up class attributes
        """
        cls.place = Place()
        cls.place.city_id = "12345"
        cls.place.user_id = "54321"
        cls.place.name = "Model"
        cls.place.description = "This is a test"
        cls.place.number_rooms = 2
        cls.place.number_bathrooms = 1
        cls.place.max_guest = 3
        cls.place.price_by_night = 50
        cls.place.latitude = 5.0
        cls.place.longitude = 7.0
        cls.place.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        """
        Teardown at the end of the test
        """
        del cls.place

    def test_is_subclass(self):
        """
        Method that checks:
            if the subclass is set correctly
        """
        place = Place()
        self.assertTrue(issubclass(place.__class__, BaseModel))

    def test_name_attr(self):
        """
        Method that checks:
            if the name of class is set correctly
        """
        place = Place()
        self.assertEqual(place.__class__.__name__, "Place")

    def test_to_dict_creates_dict(self):
        """
        Method that checks:
            if to_dict is set correctly
        """
        place = Place()
        self.assertTrue(hasattr(place, 'to_dict') is True)
        am_dict = place.to_dict
        self.assertTrue(type(am_dict), dict)

    def test_types(self):
        """
        Method that checks:
            if attr types were set correctly
        """
        place = Place()
        self.assertTrue(type(place.name) is str)
        self.assertTrue(type(place.city_id) is str)
        self.assertTrue(type(place.user_id) is str)
        self.assertTrue(type(place.description) is str)
        self.assertTrue(type(place.number_rooms) is int)
        self.assertTrue(type(place.number_bathrooms) is int)
        self.assertTrue(type(place.max_guest) is int)
        self.assertTrue(type(place.price_by_night) is int)
        self.assertTrue(type(place.latitude) is float)
        self.assertTrue(type(place.longitude) is float)
        self.assertTrue(type(place.amenity_ids) is list)

    def test_pep8_conformance_file_storage(self):
        """
        Method that tests:
            if a file meet with pep8 criteria
        """
        style = pep8.StyleGuide()
        check = style.check_files(['models/place.py'])
        self.assertEqual(
            check.total_errors,
            0,
            'PEP8 style errors: %d' % check.total_errors
        )


if __name__ == "__main__":
    unittest.main()

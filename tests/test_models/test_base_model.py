#!/usr/bin/python3
"""
Test model - BaseModel
"""

from datetime import datetime
from models.base_model import BaseModel
import models
import uuid
import unittest
import os
import pep8


class BaseModelTest(unittest.TestCase):
    """
    Base model test class
    """
    @classmethod
    def setUpClass(cls):
        """
        Setting up class attributes
        """
        cls.my_model = BaseModel()
        cls.my_model.name = "Model Test"
        cls.my_model.my_number = 89

    @classmethod
    def tearDownClass(cls):
        """
        Teardown at the end of the test
        """
        del cls.my_model
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_id_str(self):
        """
        Method to test if ID is str
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)

    def test_id_ch(self):
        """
        Method to test if ID changes with 2 objects
        """
        my_model = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model.id, my_model2.id)

    def test_dates_type(self):
        """
        Method that tests:
            if created_at and updated_at are being set correctly
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_dates_format(self):
        """
        Method that tests:
            if the UUID format is correct
        """
        my_model = BaseModel()
        self.assertIsInstance(uuid.UUID(my_model.id), uuid.UUID)

    def test_save(self):
        """
        Method that tests:
            if updated_at is being updated after using save()
        """
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_save_json_file(self):
        """
        Method that tests:
            if inf is being saved properly
        """
        my_model = BaseModel()
        my_model.save()
        with open("file.json", "r") as f:
            self.assertIn(my_model.id, f.read())

    def test_to_dict_format(self):
        """
        Method that tests:
            if to_dict returns a dictionary properly
        """
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        self.assertIsInstance(my_dict, dict)

    def test_to_dict(self):
        """
        Method that tests:
            if a directory is being properly returned
        """
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        trig = False

        if my_dict["__class__"] == "BaseModel":
            trig = True
        self.assertTrue(trig is True)

        for arg, val in my_dict.items():
            if arg in ('created_at', 'updated_at'):
                self.assertIsInstance(val, str)

    def test_pep8_conformance_base_model(self):
        """
        Method that tests:
            if a file meet with pep8 criteria
        """
        style = pep8.StyleGuide()
        check = style.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors,
            0,
            'PEP8 style errors: %d' % check.total_errors
        )


if __name__ == "__main__":
    unittest.main()

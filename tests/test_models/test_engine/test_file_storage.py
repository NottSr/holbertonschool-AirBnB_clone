#!/usr/bin/python3
"""
Test model - File storage
"""

from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import uuid
import unittest
import os
import pep8


class TestFileStorage(unittest.TestCase):
    """
    File storage test class
    """
    @classmethod
    def setUpClass(cls):
        """
        Setting up class attributes
        """
        cls.user = User()
        cls.user.email = "User@email.com"
        cls.user.first_name = "User"
        cls.user.last_name = "Test"
        cls.storage = FileStorage()
        cls.path = 'file.json'

    @classmethod
    def tearDownClass(cls):
        """
        Teardown at the end of the test
        """
        del cls.user
        del cls.storage
        del cls.path
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_returns_dict(self):
        """
        Method that tests:
            if file storage was documented
            and checks if all() returns a dict
        """
        self.assertTrue(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)

        m_test = FileStorage()
        all_ret = m_test.all()
        self.assertIsInstance(all_ret, dict)

    def test_new(self):
        """
        Method that tests:
            if file storage was documented
            and checks new() method
        """
        self.assertTrue(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)

        m_test = FileStorage()
        m_test.new(BaseModel())
        self.assertTrue(m_test.all())

    def test_save(self):
        """
        Method that tests:
            if file storage was documented
            and checks save() method
        """
        self.assertTrue(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)

        m_test = FileStorage()
        bm_test = BaseModel()
        m_test.new(bm_test)
        m_test.save()
        with open('file.json', 'r', encoding='utf-8') as r:
            json_full = r.read()
            self.assertTrue(f"BaseModel.{bm_test.id}" in json_full)

    def test_reload(self):
        """
        Method that tests:
            if file storage was documented
            and checks reload() method exists
        """
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

        m_test = FileStorage()
        self.assertTrue(hasattr(m_test, "reload"), True)

    def test_pep8_conformance_file_storage(self):
        """
        Method that tests:
            if a file meet with pep8 criteria
        """
        style = pep8.StyleGuide()
        check = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(
            check.total_errors,
            0,
            'PEP8 style errors: %d' % check.total_errors
        )


if __name__ == "__main__":
    unittest.main()

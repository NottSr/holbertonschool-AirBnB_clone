#!/usr/bin/python3
"""
Test model - State
"""

from models.base_model import BaseModel
from models.state import State
import unittest
import pep8


class TestState(unittest.TestCase):
    """
    State test class
    """
    @classmethod
    def setUpClass(cls):
        """
        Setting up class attributes
        """
        cls.state = State()
        cls.state.name = "State Test"

    @classmethod
    def tearDownClass(cls):
        """
        Teardown at the end of the test
        """
        del cls.state

    def test_is_subclass(self):
        """
        Method that checks:
            if the subclass is set correctly
        """
        state = State()
        self.assertTrue(issubclass(state.__class__, BaseModel))

    def test_name_attr(self):
        """
        Method that checks:
            if the name of class is set correctly
        """
        state = State()
        self.assertEqual(state.__class__.__name__, "State")

    def test_to_dict_creates_dict(self):
        """
        Method that checks:
            if to_dict is set correctly
        """
        state = State()
        self.assertTrue(hasattr(state, 'to_dict') is True)
        am_dict = state.to_dict
        self.assertTrue(type(am_dict), dict)

    def test_types(self):
        """
        Method that checks:
            if attr name was set correctly
        """
        state = State()
        self.assertTrue(type(state.name) is str)

    def test_pep8_conformance_file_storage(self):
        """
        Method that tests:
            if a file meet with pep8 criteria
        """
        style = pep8.StyleGuide()
        check = style.check_files(['models/state.py'])
        self.assertEqual(
            check.total_errors,
            0,
            'PEP8 style errors: %d' % check.total_errors
        )


if __name__ == "__main__":
    unittest.main()

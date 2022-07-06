#!/usr/bin/python3
"""
Test model - Review
"""

from models.base_model import BaseModel
from models.review import Review
import unittest
import pep8


class TestReview(unittest.TestCase):
    """
    Review test class
    """
    @classmethod
    def setUpClass(cls):
        """
        Setting up class attributes
        """
        cls.review = Review()
        cls.review.place_id = "12345"
        cls.review.user_id = "54321"
        cls.review.text = "This is a test text"

    @classmethod
    def tearDownClass(cls):
        """
        Teardown at the end of the test
        """
        del cls.review

    def test_is_subclass(self):
        """
        Method that checks:
            if the subclass is set correctly
        """
        review = Review()
        self.assertTrue(issubclass(review.__class__, BaseModel))

    def test_name_attr(self):
        """
        Method that checks:
            if the name of class is set correctly
        """
        review = Review()
        self.assertEqual(review.__class__.__name__, "Review")

    def test_to_dict_creates_dict(self):
        """
        Method that checks:
            if to_dict is set correctly
        """
        review = Review()
        self.assertTrue(hasattr(review, 'to_dict') is True)
        am_dict = review.to_dict
        self.assertTrue(type(am_dict), dict)

    def test_types(self):
        """
        Method that checks:
            if attr types were set correctly
        """
        review = Review()
        self.assertTrue(type(review.place_id) is str)
        self.assertTrue(type(review.user_id) is str)
        self.assertTrue(type(review.text) is str)

    def test_pep8_conformance_file_storage(self):
        """
        Method that tests:
            if a file meet with pep8 criteria
        """
        style = pep8.StyleGuide()
        check = style.check_files(['models/review.py'])
        self.assertEqual(
            check.total_errors,
            0,
            'PEP8 style errors: %d' % check.total_errors
        )


if __name__ == "__main__":
    unittest.main()

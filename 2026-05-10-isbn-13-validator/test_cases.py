import unittest
from solution import is_valid_isbn_13

class TestIsValidIsbn13(unittest.TestCase):

    def test_valid_isbn_13(self):
        """Test case for a valid ISBN-13"""
        self.assertTrue(is_valid_isbn_13("9780306406157"))
        self.assertTrue(is_valid_isbn_13("9780306406157"))

    def test_invalid_isbn_13(self):
        """Test case for an invalid ISBN-13"""
        self.assertFalse(is_valid_isbn_13("9780306406158"))
        self.assertFalse(is_valid_isbn_13("97803064061578"))

    def test_non_numeric_isbn_13(self):
        """Test case for a non-numeric ISBN-13"""
        self.assertFalse(is_valid_isbn_13("978030640615A"))
        self.assertFalse(is_valid_isbn_13("978030640615B")) 

    def test_short_isbn_13(self):
        """Test case for a short ISBN-13"""
        self.assertFalse(is_valid_isbn_13("978030640615"))
        self.assertFalse(is_valid_isbn_13("97803064061"))

    def test_long_isbn_13(self):
        """Test case for a long ISBN-13"""
        self.assertFalse(is_valid_isbn_13("97803064061578"))
        self.assertFalse(is_valid_isbn_13("978030640615789"))
        
if __name__ == "__main__":
    unittest.main()
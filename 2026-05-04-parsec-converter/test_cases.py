import unittest
from solution import convert_parsecs

class TestParsecConverter(unittest.TestCase):

    def test_odd_parsecs_to_time(self):
        """Rule: If odd, multiply by 2 (represents time in hours)"""
        self.assertEqual(convert_parsecs(1), 2)
        self.assertEqual(convert_parsecs(31), 62)
        self.assertEqual(convert_parsecs(17), 34)

    def test_even_parsecs_to_distance(self):
        """Rule: If even, multiply by 3 (represents distance in light years)"""
        # Note: 2*3=6, 88*3=264, 14*3=42
        self.assertEqual(convert_parsecs(2), 6)
        self.assertEqual(convert_parsecs(88), 264)
        self.assertEqual(convert_parsecs(14), 42)

    def test_zero_case(self):
        """Zero is technically even, so it should follow the even rule"""
        self.assertEqual(convert_parsecs(0), 0)

if __name__ == "__main__":
    unittest.main()
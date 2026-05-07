import unittest
from solution import get_greeting

class TestGetGreeting(unittest.TestCase):

    def test_morning(self):
        self.assertEqual(get_greeting("07:30"), "Good morning")

    def test_afternoon(self):
        self.assertEqual(get_greeting("14:15"), "Good afternoon")

    def test_evening(self):
        self.assertEqual(get_greeting("19:45"), "Good evening")

    def test_night(self):
        self.assertEqual(get_greeting("23:00"), "Good night")
        self.assertEqual(get_greeting("04:30"), "Good night")

    def test_invalid_time(self):
        self.assertEqual(get_greeting("25:00"), "Input not a time!")
        self.assertEqual(get_greeting("12:60"), "Input not a time!")

if __name__ == "__main__":
    unittest.main()
        
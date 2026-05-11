import unittest
from solution import get_oldest

class TestGetOldest(unittest.TestCase):
   
    def test_get_oldest_single(self):
        # Test case with a single oldest person
        people = [
            {'name': 'Alice', 'age': 30},
            {'name': 'Bob', 'age': 25},
            {'name': 'Charlie', 'age': 20}
        ]
        self.assertEqual(get_oldest(people), ['Alice'])

    def test_get_oldest(self):
        # Test case 2: Multiple people with different ages
        people = [
            {'name': 'Alice', 'age': 30},
            {'name': 'Bob', 'age': 25},
            {'name': 'Charlie', 'age': 30}
        ]
        self.assertEqual(get_oldest(people), ['Alice', 'Charlie'])

    def test_get_oldest_all_same_age(self):
        # Test case 3: All people have the same age
        people = [
            {'name': 'Alice', 'age': 30},
            {'name': 'Bob', 'age': 30},
            {'name': 'Charlie', 'age': 30}
        ]
        self.assertEqual(get_oldest(people), ['Alice', 'Bob', 'Charlie'])

if __name__ == "__main__":
    unittest.main()
import unittest
from solution import parse_url_query

class TestURLParser(unittest.TestCase):

    def test_basic_search(self):
        url = "https://example.com/search?name=Alice&age=30"
        expected = {"name": "Alice", "age": "30"}
        self.assertEqual(parse_url_query(url), expected)

    def test_programming_skill(self):
        url = "https://freecodecamp.org/learn?skill=programming&language=python"
        expected = {"skill": "programming", "language": "python"}
        self.assertEqual(parse_url_query(url), expected)

    def test_multiple_parameters(self):
        url = "https://freecodecamp.org/items?category=books&sort=asc&page=2"
        expected = {"category": "books", "sort": "asc", "page": "2"}
        self.assertEqual(parse_url_query(url), expected)

    def test_redirect_url_value(self):
        url = "https://example.com?redirect=freecodecamp.org/learn&when=now"
        expected = {"redirect": "freecodecamp.org/learn", "when": "now"}
        self.assertEqual(parse_url_query(url), expected)

if __name__ == "__main__":
    unittest.main()
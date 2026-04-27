import unittest;
from solution import get_word_score;

class TestWordScore(unittest.TestCase):

    def test_hi(self):
        self.assertEqual(get_word_score("hi"), 17)

    def test_hello(self):
        self.assertEqual(get_word_score("hello"), 52)

    def test_hippopotamus(self):
        self.assertEqual(get_word_score("hippopotamus"), 169)

    def test_freeCodeCamp(self):
        self.assertEqual(get_word_score("freeCodeCamp"), 94)

if __name__ == '__main__':
    unittest.main()
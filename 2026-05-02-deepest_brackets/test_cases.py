import unittest
from solution import get_deepest_brackets

class TestURLParser(unittest.TestCase):

    def test_simple_nesting(self):
        self.assertEqual(get_deepest_brackets("(hello (world))"), "world")

    def test_square_brackets(self):
        self.assertEqual(get_deepest_brackets("[outer [inner] outer]"), "inner")

    def test_multiple_sibling_brackets(self):
        # Even with multiple brackets, it should find the deepest 'e'
        self.assertEqual(get_deepest_brackets("{a{b}c{d{e}f}g}"), "e")

    def test_complex_mixed_brackets(self):
        url = "[the {quick (brown [fox] jumped) over (the) lazy} dog]"
        self.assertEqual(get_deepest_brackets(url), "fox")

    def test_highly_fragmented_string(self):
        # Testing the specific case with single character deep results
        self.assertEqual(get_deepest_brackets("f[(r)e{e}C{o[(d){e(C)}a]m}]p"), "C")
if __name__ == "__main__":
    unittest.main()
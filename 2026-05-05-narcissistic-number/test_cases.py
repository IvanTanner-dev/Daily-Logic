import unittest
from solution import is_narcissistic

class TestNarcissisticNumbers(unittest.TestCase):

        def test_narcissistic_numbers(self):
            self.assertTrue(is_narcissistic(0))
            self.assertTrue(is_narcissistic(153))  
            self.assertTrue(is_narcissistic(370))  
            self.assertTrue(is_narcissistic(371))  
            self.assertTrue(is_narcissistic(407))  
    
        def test_non_narcissistic_numbers(self):
            self.assertFalse(is_narcissistic(123)) 
            self.assertFalse(is_narcissistic(10))   
            self.assertFalse(is_narcissistic(100)) 

if __name__ == "__main__":
    unittest.main()
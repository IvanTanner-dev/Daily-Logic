import unittest
from solution import get_allergen_friendly_meals

class TestAllergenFriendlyMeals(unittest.TestCase):

    def test_allergen_friendly_meals(self):
        """Test that meals with no allergens are returned"""
        meals = [
        ["Pasta", ["wheat", "eggs"]],
        ["Salad", ["lettuce", "tomatoes"]],
        ["Sandwich", ["bread", "cheese"]]
        ]
        allergens = ["shellfish"]
        self.assertEqual(get_allergen_friendly_meals(meals, allergens), ["Pasta", "Salad", "Sandwich"])
        

    def test_meals_with_allergens(self):
        """Test that meals with allergens are not returned"""
        meals = [
        ["Pasta", ["wheat", "eggs"]],
        ["Salad", ["lettuce", "tomatoes"]],
        ["Sandwich", ["bread", "cheese"]]
        ]
        allergens = ["wheat", "bread"]
        self.assertEqual(get_allergen_friendly_meals(meals, allergens), ["Salad"])

    def test_no_allergen_friendly_meals(self):
        """Test that an empty list is returned if no meals are allergen-friendly"""
        meals = [
        ["Pasta", ["wheat", "eggs"]],
        ["Salad", ["lettuce", "tomatoes"]],
        ["Sandwich", ["bread", "cheese"]]
        ]
        allergens = ["wheat", "bread", "lettuce", "tomatoes", "cheese"]
        self.assertEqual(get_allergen_friendly_meals(meals, allergens), [])
    
if __name__ == "__main__":
    unittest.main()
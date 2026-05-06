# Allergen Friendly Meals

## Lightbulb Moments

> **Data Structures: Sets and Disjoint**
> The "Jump" vs. The "Walk": I learned that searching a List is like walking down a row of lockers ($O(n)$), while searching a Set or Dict is like jumping straight to a specific mailbox ($O(1)$) using a Hash Function.

> Mathematical Intersection: I discovered set.isdisjoint(), which is the coding equivalent of checking if two circles in a Venn Diagram have zero overlap.

> Intent-Based Selection: I identified that Lists are for processing every item (like doubling numbers), while Sets are for filtering and membership testing.

> **The Art of Writing Tests**
> Atomic Test Functions: Broke tests into individual named functions (e.g., test_no_allergen_friendly_meals). This ensures that if one check fails, the others keep running, providing a full "health report."

> Documentation via Code: You used Docstrings ("""...""") to describe the intent of each test. This makes your terminal output (python -m unittest -v) readable to humans, not just machines.

## The Challenge

Given an array of meals and an array of allergens to avoid, return the names of all the meals that contain none of the given allergens.

Each meal is in the format [meal, allergens], where meal is the name of the meal, and allergens is an array of the allergens the meal contains. For example, ["pasta", ["wheat", "milk"]].
Allergens to avoid will be an array of strings.
Return safe meal names in the same order given. If no meal is safe, return an empty array.

### Example

get_allergen_friendly_meals([["pasta", ["wheat", "milk"]], ["salad", ["nuts"]]], ["milk"]) should return ["salad"].

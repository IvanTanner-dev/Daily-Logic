# Array Sum Finder

## The Challenge

Given an array of numbers and a target value, find the **first subset** of two or more numbers that adds up to that target.

### Rules:

- **Index Priority:** The "first" subset is defined by the lowest possible indices, prioritizing the earliest index first.
- **No Reuse:** Each number in the array may only be used once.
- **Order:** Return the matching numbers as an array in the order they appear in the original array.
- **Edge Cases:** If no valid subset exists, return `"Sum not found"`.

---

## Lightbulb Moments

### 1. Using `itertools.combinations`

Since the solution could consist of two numbers or many more, I couldn't hard-code the number of loops. Using `itertools` allowed me to dynamically generate every possible combination length without knowing the answer in advance.

### 2. Storing Data as Tuples

To satisfy the "Index Priority" rule, I needed to keep track of _where_ the numbers came from. I stored each match as a nested tuple: `(indices, values)`. This kept the metadata (position) tied to the data (the numbers).

### 3. Exploiting Python's `.sort()`

A major takeaway was learning how Python handles tuple comparison. Because Python sorts tuples element-by-element (lexicographical order), sorting a list of index-tuples like `(0, 1, 2)` and `(0, 4)` automatically prioritizes the one with the lowest subsequent index.

---

## Usage & Examples

```python
from solution import find_sum

# Returns [1, 2, 3] (indices 0, 1, 2) instead of [1, 5] (indices 0, 4)
print(find_sum([1, 2, 3, 4, 5], 6))

# Returns "Sum not found" if no combination hits the target
print(find_sum([7, 9, 4], 10))

---

```

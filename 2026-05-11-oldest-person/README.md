# Oldest Person

## Lightbulb Moments

> **Data Structures**
> Mastering the "Russian Doll" nesting of lists within dictionaries.

> **Memory Management**
> Learning the difference between List Comprehensions (eager evaluation) and Generator Expressions (lazy evaluation).

> **Computational Complexity**
> Understanding that while we can optimize memory ($O(1)$), we must still visit every element ($O(n)$) to guarantee an accurate result in an unsorted list.

## The Challenge

This project provides an efficient solution for extracting the highest-valued entries from a dataset of key-value pairs. Specifically, it handles a list of nested dictionaries (JSON-style data) to identify individuals with the greatest recorded age, accounting for ties and large datasets.

### Example

`get_oldest([{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }])` should return `["Alice"]`.

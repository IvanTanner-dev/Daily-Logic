# Narcissistic Number

## Lightbulb Moments

[!TIP]

> **Avoid Redundant Computation**
> Realised that calculating len(str(n)) inside the generator expression is inefficient. Storing the length in a variable first is a "micro-optimization" that matters as the input grows.

> **Strings are Collections**
> Realised that Python treats the string "153" exactly like the list ["1", "5", "3"]

> **Explicit Casting**
> Learned that Python won't "guess" that you want a number; you have to explicitly use int() to cross the bridge from text to math

> **Attribute Persistence**
> Noticed that len() works on the string to give you the count, but you still need the integer conversion to perform the actual arithmetic.

## The Challenge

Given a positive integer, determine whether it is a narcissistic number.

A number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the number itself.

### Example

153 has 3 digits, and 13 + 53 + 33 = 153, so it is narcissistic.

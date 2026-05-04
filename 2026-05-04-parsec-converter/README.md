# Parsec Converter

## Lightbulb Moments

> **Branchless Programming**
> Realised that you can replace logic gates (if/else) with data structures (lists/dicts) to make the code more "functional".

## The Challenge

In a distant galaxy, parsecs are used to measure both time and distance. Given an integer number of parsecs, return its equivalent in time or distance.

If the given integer is odd, it represents time. If it's even, it represents distance.
Use these conversion rates:

| Parsecs | Time/Distance |
| :------ | :------------ |
| **1**   | 2 hours       |
| **2**   | 6 light years |

Return the converted value as an integer.

### Example

convert_parsecs(88) should return 264.

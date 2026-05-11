# ISBN-13 Validator

## Lightbulb Moments

> **The "Zero Trap" (Truthiness)**
> I discovered that using if int(value): as a filter accidentally skips zeros because 0 is "Falsey" in Python. I learned to use .isdigit() to check for numbers without excluding zero.

> **Early Exit Strategy**
> By checking for forbidden characters (not in "0123456789-") at the very beginning of the loop, I optimized the code to stop immediately rather than performing useless math on invalid data.

> **Position vs. Value**
> I realised that the "Even/Odd" position (count) must track how many digits have been processed so far, regardless of whether a hyphen was just skipped.

> **Exact Constraint Logic**
> I learned that checking count > 13 wasn't enough. Using count == 13 ensures the code handles strings that are both too long and too short.

## The Challenge

Create a function is_valid_isbn_13(s) that determines if a given string is a valid ISBN-13 based on the following constraints:

Characters: Must only contain digits (0-9) and hyphens (-). Any other character (like letters) immediately renders it invalid.

Length: Must contain exactly 13 digits after hyphens are ignored.

Checksum: Uses the weighted sum algorithm:

    Multiply digits in odd positions by 1.

    Multiply digits in even positions by 3.

The total sum must be divisible by 10 (total % 10 == 0).

### Example

`is_valid_isbn_13("9780306406157")` should return `True`.

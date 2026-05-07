# Good Day

## Lightbulb Moments

> **Chained Comparisons**
> Python allows you to write comparisons exactly like you would in a math textbook (e.g., $5 \leq x < 12$).

> **The "Fall-through" Logic**
> Learned that if you order your if statements correctly, you can often avoid complex or conditions (like the one for "Good night") by letting the remaining cases "fall through" to the final return.

> **Slicing over Splitting**
> Discovered that when the structure of a string is fixed (like a digital clock), slicing ([:2]) is a direct way to grab data without the overhead of splitting.

## The Challenge

Given a time string in "HH:MM" format (24-hour clock), return:

"Good morning" for times 05:00 to 11:59
"Good afternoon" for times 12:00 to 17:59
"Good evening" for times 18:00 to 21:59
"Good night" for times 22:00 to 04:59

### Example

get_greeting("06:30") should return "Good morning"

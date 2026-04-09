Goal: To output the next bingo number for a given input. A bingo number is a letter followed by a two digit number as shown in this table:

| Letter | Number Range |

| **B** | 1 - 15 |
| **I** | 16 - 30 |
| **N** | 31 - 45 |
| **G** | 46 - 60 |
| **O** | 61 - 75 |

Examples: B15 -> I16, O66 -> O67

My Approach: I split the original string into two parts, representing the second part as an integer, then adding one to it which will solve the problem for most cases. I then set up if/elif conditionals to check the edge cases and convert them to the next letter. For example B15 + 1 = B16 but B16 is not a bingo number so it is refactored into I16

Lightbulb Moment: == is for comparison (asking a question) whereas = is for assignment (setting a value). "11" is a string whereas int("11") is a number which can be used to apply mathematical operations.

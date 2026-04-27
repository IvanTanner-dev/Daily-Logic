# Word Score Calculator

## Lightbulb Moments

> [!TIP]
> **Optimized Mapping via Hash Map**
> Instead of using iterative conditional logic or repetitive string searching, this implementation utilizes a **Dictionary (Hash Map)** to store character-to-value mappings. This ensures **O(1) constant-time lookup** for each letter's score, significantly increasing performance compared to linear search methods.

> [!IMPORTANT]
> **Declarative Data Transformation**
> The core logic leverages **List Comprehensions** to transform the input string into a numerical sequence. By moving from an imperative for-loop to a declarative comprehension, the code is more "Pythonic"—improving readability and reducing the likelihood of side effects during the aggregation process.

## The Challenge

The script maps each letter to its corresponding value and returns the total sum. It is case-insensitive, so "Hi" and "hi" will return the same score.

### Example Scores

| Word             | Score |
| :--------------- | :---- |
| **hi**           | 17    |
| **hello**        | 52    |
| **freeCodeCamp** | 94    |

## Usage

You can use the function by importing it into your own scripts:

```python
from solution import get_word_score

print(get_word_score("Python"))
```

# Earth Day Cleanup Crew

## Lightbulb Moments

- **Dict-First Architecture:** Recognized the dictionary as a Hash Map, providing **O(1) constant time** lookups for item values instead of inefficient list searching.
- **Type Guarding (Defensive Coding):** Implemented `isinstance()` checks to create "fork in the road" logic—gracefully handling mixed data types (strings vs. lists) without runtime crashes.
- **Modular Assembly:** Organized the logic into a **linear pipeline** (Value $\rightarrow$ Streak $\rightarrow$ Multiplier) to ensure the mathematical order of operations remained consistent.
- **Stateful Looping:** Leveraged `enumerate()` and external state variables to give the loop a **"memory,"** allowing the program to track complex scoring across iterations.
- **Mathematical Sequencing:** Developed an **O(n) solution** for the $5n$ multiplier rule using floor division (`//`) and modulo (`%`) operators to handle scaling bonuses.

## The Challenge

Given an array of items return the total cleanup score based on this table:

Given items will be one of:

| Item            | Base Value |
| :-------------- | :--------- |
| **bottle**      | 10         |
| **can**         | 6          |
| **bag**         | 8          |
| **tire**        | 35         |
| **straw**       | 4          |
| **cardboard**   | 3          |
| **newspaper**   | 3          |
| **shoe**        | 12         |
| **electronics** | 25         |
| **battery**     | 18         |
| **mattress**    | 38         |

A Rare item is represented as ["rare", value]. For example, ["rare", 80]. Rare items do not get a streak bonus.

Streak bonus: If the same item appears consecutively, it gets increasing bonus points.

First consecutive occurrence: base value
Second: base value + 1
Third: base value + 2
etc.
Fifth Item Multiplier: Every fifth item collected gets a multiplier.

Fifth item: *2
Tenth item: *3
etc.
Apply the multiplier after calculating any bonuses.

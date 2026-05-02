# Deepest Brackets

## Lightbulb Moments

> [!TIP]
> **Altitude Tracking (Depth Logic)**
> Visualized nested structures as a climber moving up and down levels. Used a current_depth variable to track position and a max_depth variable to record the "high-water mark."

> [!IMPORTANT]
> **The Dethroning Pattern**
> Implemented a "reset" mechanic: whenever the climber reaches a new record altitude, the previous "deepest" notes are discarded (deepest_content = "") to make room for the truly deepest data.

## The Challenge

Given a string containing balanced brackets, return the content of the deepest nested brackets.

Brackets can be any of the three types: (), [], and {}.
The input will always have a single deepest group.

### Example

"(hello (world))" should return "world".

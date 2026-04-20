# Acronym Finder

## The Challenge
Given an acronym string, return the full name of the organization from the following pool:
- NASA, CIA, FBI, DOJ, WHO, EPA

## Lightbulb Moments 
* **Hash Maps for Speed:** Swapped a `for` loop for a Python `dict`. This turned a linear search into an **O(1) constant time** lookup.
* **Keep It Simple (KISS):** Realized that for 6 static items, a manually defined dictionary is more readable and less prone to "acronym edge-case" errors than a generator script.
* **Environment Hygiene:** Initialized a `venv` to ensure that testing remained isolated from system-wide Python packages.

## Quick Start
```python
from solution import find_org

# Instant lookup
print(find_org("NASA")) # "National Avocado Storage Authority"
## Problem

Determine if a word exists in a 2D grid of letters by connecting adjacent letters.

**Example:**
```text
board = [
  ['C', 'A', 'T', 'D'],
  ['O', 'G', 'O', 'E'],
  ['D', 'O', 'G', 'F']
]

Given word = "DOG", return true
Given word = "CAT", return true
Given word = "FOG", return false
```

**Movement Rules:**
- Can move up, down, left, or right
- Cannot reuse the same cell
- Must follow the exact word sequence

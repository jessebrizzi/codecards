## Problem

Given an array of numbers, create a new array where each element is the product of all numbers in the original array except the number at that index.

**Example:**
```text
Input: [3, 5, 2, 4]
Output: [40, 24, 60, 30]
Explanation:
- 40 = 5 * 2 * 4 (product of all numbers except 3)
- 24 = 3 * 2 * 4 (product of all numbers except 5)
- 60 = 3 * 5 * 4 (product of all numbers except 2)
- 30 = 3 * 5 * 2 (product of all numbers except 4)
```

**Requirements:**
- Must run in O(n) time
- Can't use division

**Follow up:**
- Must use constant space (excluding output array)
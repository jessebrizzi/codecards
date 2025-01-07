## Problem

Find a target number in a sorted array that has been rotated at an unknown point.

**Example 1:**
```text
Input: [6, 7, 8, 1, 2, 3, 4, 5], target = 3
Output: 5
Explanation: The array is rotated at index 3, and target 3 is found at index 5
```

**Example 2:**
```text
Input: [9, 10, 2, 4, 5, 6, 7], target = 8
Output: -1
Explanation: The target number 8 is not present in the array
```

**Key Points:**
- Array was originally sorted in ascending order
- Rotated at some unknown pivot point
- No duplicate numbers exist
- Must run in O(log n) time complexity
- Return index of target or -1 if not found

## Problem

Design a system to efficiently calculate the median of numbers received from a continuous data stream.
Implement the MedianFinder class:
- `addNum(int num)` adds the integer `num` from the data stream.
- `findMedian()` returns the median of all elements so far.
**Example:**
```text
Operations: ["addNum", "addNum", "findMedian", "addNum", "findMedian"]
Inputs: [[5], [8], [], [3], []]
Output: [null, null, 6.5, null, 5.0]

Explanation:
1. addNum(5) → Numbers: [5]
2. addNum(8) → Numbers: [5, 8]
3. findMedian() → (5 + 8) / 2 = 6.5
4. addNum(3) → Numbers: [3, 5, 8]
5. findMedian() → 5.0 (middle value)
```

**Requirements:**
- Must handle continuous stream of numbers
- Median calculation must be efficient
- Numbers can be positive or negative
- Must handle both odd and even counts of numbers

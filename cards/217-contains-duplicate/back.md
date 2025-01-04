## Complexity
Time: `O(n)`
Space: `O(n)`

## Intuition

"Single pass", using a set to keep track of previously seen items until you find a second item that satisfies the requirement.

But we can also just convert the array to a set and check if it's length is equal to the original array length which is faster in python.

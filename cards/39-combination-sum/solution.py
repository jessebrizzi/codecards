class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        nums.sort()  # not contribute to time complexity
        backtrack_combination_sum(result, [], candidates, target, 0)
        return result

    def backtrack_combination_sum(result, temp_list, nums, remain, start):
        if remain < 0:
            return
        elif remain == 0:
            result.append(temp_list[:])
        else:
            for i in range(start, len(nums)):
                temp_list.append(nums[i])
                backtrack_combination_sum(result, temp_list, nums, remain - nums[i], i)  # not i + 1 because we can reuse same elements
                temp_list.pop()
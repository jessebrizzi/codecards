class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()

        i = 0
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1

            while j < k:

                triple_sum = nums[i] + nums[j] + nums[k]

                if triple_sum == 0:     # record result and move both j and k to next new numbers
                    results.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif triple_sum > 0:    # decrement k to next new number
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                else:                   # increment j to next new number
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

            i += 1                      # increment i to next new number
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1

        return results
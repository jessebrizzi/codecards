class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
						# if the left side of the array is not rotated
            if nums[l] <= nums[m]:
								# if the target is on the left side 
                if target >= nums[l] and target < nums[m]:
                    r = m -1
                else:
                    l = m + 1
            # the left side is rotated
						else:
								# if the target is on thr right side
                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
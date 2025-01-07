class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return True
            
            while l < m and nums[l] == nums[m]: # tricky part
                l += 1
            
            # the first half is ordered
            if nums[l] <= nums[m]:
                 # target is in the first half
                if target >= nums[l] and target < nums[m]:
                    r = m -1
                else:
                    l = m + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False
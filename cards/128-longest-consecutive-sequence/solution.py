class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        out = 0
        
        for n in s:
            if n-1 not in s:
                seq = 0
                while n in s:
                    seq += 1
                    n += 1
                out = max(out, seq)
        
        return out
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        out = min(height[l], height[r]) * (r - l)
        
        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            out = max(out, min(height[l], height[r]) * (r - l))
        
        return out
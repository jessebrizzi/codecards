class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l = [1]
        for n in nums:
            l.append(n * l[-1])
        r = [1]
        for n in nums[::-1]:
            r.append(n * r[-1])
            
        out = []
        N = len(nums)
        for i in range(N):
            out.append(l[i] * r[N-i-1])
            
        return out
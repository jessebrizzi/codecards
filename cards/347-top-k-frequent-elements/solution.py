class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
                
        d = [(v, k) for k, v in d.items()]
        d.sort()
        
        return [k for _, k in d[-k:]][::-1]
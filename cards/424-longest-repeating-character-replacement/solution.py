class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # base case
        if len(s) < k:
            return len(s)
        
        # prep condition
        c = collections.defaultdict(int)
        max_val = 0
        
        # pointers
        l,r = 0,0
        out = k+1
        
        while r < len(s):
            # update condition
            c[s[r]] += 1
            max_val = max(c[s[r]], max_val)
            
            # check conditions met
            if r-l+1 - max_val <= k:
                out = max(out, r-l+1)
                
            while r-l+1 - max_val > k:
                # update condition
                c[s[l]] -= 1
                
                l += 1
            r += 1
        
        return out
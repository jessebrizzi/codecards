class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # make condition tracker
        c = collections.Counter(t)
        to_match = len(c)
        
        # init 2 pointers and out
        out = (0, len(s)+1)
        l, r = 0, 0
        
        # expand the window
        while r < len(s):
            # update condition
            if s[r] in c:
                c[s[r]] -= 1
                if c[s[r]] == 0:
                    to_match -= 1
            
            # if condition met
            while to_match == 0:
                # track optimal
                if out[1] - out[0] > r - l:
                    out = (l, r)
                # shrink window, update condition
                if s[l] in c:
                    c[s[l]] += 1
                    if c[s[l]] == 1:
                        to_match += 1
                l += 1
            r += 1     
        
        # if nothing found
        if out[1] == len(s)+1:
            return ''
        
        return s[out[0]: out[1]+1]
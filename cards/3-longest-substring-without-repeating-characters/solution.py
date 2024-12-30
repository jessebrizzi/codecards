class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()
        out = 0

        i,j = 0,0
        
        while j < len(s):
            c = s[j]
            if c in d:
                while i < j:
                    _c = s[i]
                    d.remove(_c)
                    i += 1
                    if _c == c:
                        break
            else:
                d.add(c)
                out = max(j - i + 1, out)
                j += 1
        
        return out
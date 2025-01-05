class Solution:
    def isPalindrome(self, s: str) -> bool:  
        valid = set(string.ascii_lowercase + string.digits)
        s = [c for c in s.lower() if c in valid]
        
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return False
            r -= 1
            l += 1
            
        return True
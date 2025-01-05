from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        
        for word in strs:
            letters = [c for c in word]
            letters.sort()
            sorted_word = ''.join(letters)
            d[sorted_word].append(word)
        
        return list(d.values())
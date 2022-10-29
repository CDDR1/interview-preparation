class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        map = {}
        for c in s:
            if c in map:
                map[c] += 1
            else:
                map[c] = 1
        
        freq = map[s[0]]
        
        for c in s:
            if map[c] != freq:
                return False
            
        return True
    
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Arrays & Hashing
# Time used: 7min
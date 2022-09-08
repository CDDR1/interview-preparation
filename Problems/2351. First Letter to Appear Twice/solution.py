class Solution:
    def repeatedCharacter(self, s: str) -> str:
        map = {}
        
        for c in s:
            if c in map:
                return c
            else:
                map[c] = True

# Time Complexity: O(n)
# Space Complexity: O(n)
# Time used: 2min
# Pattern: arrays & Hashing
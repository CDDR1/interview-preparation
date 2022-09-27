class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        seen = set()
        counter = 0
        
        for i in range(len(s) - 2):
            seen.add(s[i])
            seen.add(s[i + 1])
            seen.add(s[i + 2])
            if len(seen) == 3:
                counter += 1
            seen.clear()
        
        return counter
    
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Sliding Window
# Time used: 25min
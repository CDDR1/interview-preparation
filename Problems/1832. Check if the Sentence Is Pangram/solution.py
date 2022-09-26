class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        
        for c in sentence:
            if c not in seen:
                seen.add(c)
            if len(seen) == 26:
                return True
        
        return False
    
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Arrays & Hashing
# Time used: 2min
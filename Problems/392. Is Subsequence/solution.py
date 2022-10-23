class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        
        while (i < len(s)) and (j < len(t)):
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return True if i == len(s) else False
    
# Time complexity: O(n), where n is the length of t
# Space complexity: O(1)
# Pattern: Two Pointers
# Time used: 37min before looking at NeetCode's video solution.
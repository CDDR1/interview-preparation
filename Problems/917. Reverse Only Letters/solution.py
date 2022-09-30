class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        s = list(s)
        
        while l < r:
            while (90 < ord(s[l]) < 97 or ord(s[l]) < 65) and (l < r):
                l += 1
            while (90 < ord(s[r]) < 97 or ord(s[r]) < 65) and (l < r):
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        return "".join(s)
    
# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Two Pointers
# Time used: 22min
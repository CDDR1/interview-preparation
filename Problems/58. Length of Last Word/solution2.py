class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = len(s) - 1
        
        while s[i] == " ":
            i -= 1
        while (i >= 0) and (s[i] != " "):
            count += 1
            i -= 1
            
        return count
                
    
# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Arrays

# =========================================================
# this is a more optimal approach because we start counting 
# from the end of the string, which means that we have to 
# do less iterations. 
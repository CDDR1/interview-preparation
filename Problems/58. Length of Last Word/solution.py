class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastWord = ""
        
        for index, c in enumerate(s):
            if (c != " "):
                if (s[index - 1] == " ") and (len(lastWord) > 0):
                    lastWord = ""
                lastWord += c
                
        return len(lastWord)
    
# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Arrays
# Time used: 9min
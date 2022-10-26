class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        s1 = ""
        for i in range(len(word1)):
            j = 0
            while j < len(word1[i]):
                s1 += word1[i][j]
                j += 1
                
        s2 = ""
        for i in range(len(word2)):
            j = 0
            while j < len(word2[i]):
                s2 += word2[i][j]
                j += 1
                
        return s1 == s2
                
        
# Time complexity: O(n + m)
# Space complexity: O(n + m)
# Pattern: Arrays
# Time used: 37min
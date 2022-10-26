class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        l, r = 0, 0
        
        while (l < len(word1)) and (r < len(word2)):
            if l == 0:
                # add l and increment
                ans += word1[l]
                l += 1
            else:
                if l > r:
                    # add r and increment
                    ans += word2[r]
                    r += 1
                else:
                    # add l and increment
                    ans += word1[l]
                    l += 1
                    
        if l == len(word1):
            # add what is left of word2
            while r < len(word2):
                ans += word2[r]
                r += 1
        elif r == len(word2):
            # add what is left of word1
            while l < len(word1):
                ans += word1[l]
                l += 1
        
        return ans
    
# Time complexity: O(n + m), where n is the length of word1 and m is the length of word2
# Space complexity: O(1)
# Pattern: Two Pointers
# Time used: 12min
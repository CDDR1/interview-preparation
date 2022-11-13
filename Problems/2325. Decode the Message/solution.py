class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        ans = ""
        map = {}
        letter = 97
        
        for c in key:
            if len(map) == 26:
                break
            if c not in map and c != " ":
                map[c] = chr(letter)
                letter += 1
                
        for c in message: 
            if c == " ":
                ans += c
            else:
                ans += map[c]
                
        return ans
    
# ==============================================================
# n = length of key
# m = length of message
# 
# Time complexity: O(26 + m), which is equal to O(m)
# Space complexity: O(26), which is equal to O(1)
# Pattern: Arrays & Hashing
# Time used: 12min
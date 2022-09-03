class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map = {}
        
        for char in s:
            if char in map:
                map[char] = map[char] + 1
            else:
                map[char] = 1
                
        for char in t:
            if char in map:
                map[char] = map[char] - 1
        
        for char in s:
            if map[char] != 0:
                return False
            
        return True

# Time Complexity: O(n)
# Space Complexity: O(n)
# Time used: 13min      
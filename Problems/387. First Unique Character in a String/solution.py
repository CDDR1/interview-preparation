class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        
        for i in s:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
                
        for index, i in enumerate(s):
            if map[i] == 1:
                return index
            
        return -1
    
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time Used: 3min
# Patter: Arrays & Hashing
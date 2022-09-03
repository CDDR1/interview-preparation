class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        map = {}
        
        for i in arr:
            if i in map:
                map[i] = map[i] + 1
            else:
                map[i] = 1
                
        counter = 0
        for i in arr:
            if map[i] == 1:
                counter = counter + 1
            if counter == k:
                return i
            
        return ""
    
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time used: 12min
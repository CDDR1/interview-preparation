class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        result = []
        map = {}
        
        for num in nums: 
            map[num] = True
            
        for n in range(1, len(nums) + 1):
            if n not in map:
                result.append(n)
                
        return result
            
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time used: about 15 mins
# Pattern: Arrays & Hashing
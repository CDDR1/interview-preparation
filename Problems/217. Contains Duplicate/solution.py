class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        
        for num in nums: 
            if num in map:
                return True
            else:
                map[num] = True 
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)
# Time used: 4min
# Pattern: Arrays & Hashing
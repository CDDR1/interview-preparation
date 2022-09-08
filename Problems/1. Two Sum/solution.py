# Return the indices
# nums will have at list 2 numbers

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i, num in enumerate(nums):
            if target - num in map:
                return [i, map[target - num]]
            else:
                map[num] = i

# Time Complexity: O(n)
# Space Complexity: O(n)
# Time used: 16min
# Pattern: Arrays & Hashing
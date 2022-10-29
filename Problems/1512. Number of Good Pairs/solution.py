class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        map = {}
        ans = 0
        for i, num in enumerate(nums):
            if num in map:
                ans += map[num]
                map[num] += 1
            else:
                map[num] = 1
                
        return ans
    
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Arrays & Hashing
# Time used: 13min
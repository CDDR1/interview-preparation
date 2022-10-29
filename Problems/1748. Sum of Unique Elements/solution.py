class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
                
        ans = 0
        for num in nums:
            if map[num] == 1:
                ans += num
        
        return ans
    
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Arrays & Hashing
# Time used: 2min
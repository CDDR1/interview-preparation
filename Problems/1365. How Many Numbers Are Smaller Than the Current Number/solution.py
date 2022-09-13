class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums) # time O(nlogn)
        seen = {} # space O(n)
        result = [] # space O(n)
        
        for index, num in enumerate(sortedNums): # time O(n)
            if num not in seen: # time O(1)
                seen[num] = index # time O(1)
        
        for num in nums: # time O(n)
            result.append(seen[num]) # time O(1)
                
        return result
    
# Time complexity: O(nlogn)
# Space complexity: O(n)
# Time used: 24min
# Pattern: Arrays & Hashing
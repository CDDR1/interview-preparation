class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
            
        if target < nums[m]:
            return m
        else:
            return m + 1
        
# Time complexity: O(log n)
# Space complexity: O(1)
# Pattern: Binary Search
# Time used: over 30mins
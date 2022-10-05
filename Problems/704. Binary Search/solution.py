class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = len(nums) // 2
        
        while l <= r:
            if target > nums[m]:
                l = m + 1
                m = l + (r - l) // 2
            elif target < nums[m]:
                r = m - 1
                m = l + (r - l) // 2
            else:
                return m
        
        return -1
    
# Time complexity: O(log n)
# Space complexity: O(1)
# Pattern: Binary Search
# Time used: over 30min
        
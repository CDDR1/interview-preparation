class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = len(nums) // 2
        
        while l <= r:
            m = (r + l) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        
        return -1
    
# Time complexity: O(log n)
# Space complexity: O(1)
# Pattern: Binary Search
        
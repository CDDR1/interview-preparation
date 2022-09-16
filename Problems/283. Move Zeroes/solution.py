class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]: # if nums[r] is greater than 0
                nums[r], nums[l] = nums[l], nums[r]
                l += 1

# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Two Pointers
# Time used: over an hour (had to look NeetCode's video)                
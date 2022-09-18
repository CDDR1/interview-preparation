class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        counter = 0
        
        while l <= r:
            if nums[r] == val:
                nums[r] = "_"
                r -= 1
                counter += 1
            while nums[l] == val:
                nums[l] = nums[r]
                nums[r] = "_"
                r -= 1
                counter += 1
            l += 1
            
        return len(nums) - counter

# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Two Pointers
# Time used: 41min
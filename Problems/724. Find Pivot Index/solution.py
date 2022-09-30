class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # BRUTE FORCE SOLUTION O(n^2):
        # for i in range(len(nums)):
        #     lSum = 0
        #     rSum = 0
        #     for j in range(len(nums)):
        #         if j == i: 
        #             continue
        #         if j < i:
        #             lSum += nums[j]
        #         else:
        #             rSum += nums[j]
        #     if lSum == rSum:
        #         return i
        # return - 1
        
        #OPTIMAL SOLUTION: 
        lSum = 0
        rSum = 0
        
        for i in range(1, len(nums)):
            rSum += nums[i]
            
        for i in range(len(nums)):
            if lSum == rSum:
                return i
            lSum += nums[i]
            if i + 1 < len(nums):
                rSum -= nums[i + 1]
        return -1
            
    
    # Time complexity: O(n)
    # Space complexity: O(1)
    # Pattern: Arrays & Hashing
    # Time used: 26min
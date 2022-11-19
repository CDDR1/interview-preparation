class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        
        prefix = 1
        for i in range(len(nums)):
            ans.append(prefix)
            prefix *= nums[i]
            
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
            
        return ans

# Time complexity: O(n)
# Space complexity: O(1), because we're not taking into account the output array. 
# Pattern: Arrays        
# Time used before looking at solution: 15min
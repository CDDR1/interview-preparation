class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minPrefixSum = nums[0]
        runningSum = 0
        
        for num in nums:
            runningSum += num
            minPrefixSum = min(minPrefixSum, runningSum)
            
        # minPrefixSum + x = 1
        # x = 1 - minPrefixSum
        startValue = 1 - minPrefixSum
        return startValue if startValue > 0 else 1
    
# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Arrays
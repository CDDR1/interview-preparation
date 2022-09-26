class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        for i in range(k):
            currSum += nums[i]
        
        maxSum = currSum
        
        for i in range(1, len(nums) - (k - 1)):
            currSum -= nums[i - 1]
            currSum += nums[i + (k - 1)]
            maxSum = max(maxSum, currSum)
            
        return maxSum / k

# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Sliding Window
# Time used: 44min in total (Had to look at the solution)
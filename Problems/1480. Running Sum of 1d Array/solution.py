class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        runningSum = 0
        for num in nums:
            runningSum += num
            ans.append(runningSum)
            
        return ans
    
# Time complexity: O(n)
# Space complexity: O(1) without taking into account the space taken by the output array
# Pattern: Arrays
# Time used: 2min
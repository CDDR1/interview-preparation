class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1
        keepLooping = True
        
        while keepLooping: 
            keepLooping = False
            runningSum = startValue
            for num in nums:
                runningSum += num
                if runningSum < 1:
                    startValue += 1
                    keepLooping = True
                    break
        
        return startValue
    
# Time complexity: O(n * startValue)
# Space complexity: O(1)
# Pattern: Arrays
# Time used: 8min
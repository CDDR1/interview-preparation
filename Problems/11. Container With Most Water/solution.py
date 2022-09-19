class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        
        lowestLine = min(height[l], height[r])
        maxArea = lowestLine * (r - l)
        
        while l < r:
            lowestLine = min(height[l], height[r])
            currArea = lowestLine * (r - l)
            maxArea = max(maxArea, currArea)
            if height[r] == lowestLine:
                r -= 1
            elif height[l] == lowestLine:
                l += 1
        
        return maxArea
    
# Time complexity: O(n)
# Space complexity: O(1)
# Time used: 74min
# Pattern: Two Pointers
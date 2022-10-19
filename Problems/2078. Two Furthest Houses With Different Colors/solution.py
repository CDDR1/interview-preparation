class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxDisL = 0
        for index, c in enumerate(colors):
            if c != colors[0]:
                currDis = index - 0
                maxDisL = max(maxDisL, currDis)
                
        maxDisR = 0
        for i in range(len(colors) - 1, -1, -1):
            if colors[i] != colors[-1]:
                currDis = len(colors) - 1 - i
                maxDisR = max(maxDisR, currDis)
                
        return max(maxDisL, maxDisR)
    
# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Arrays, Greedy
# Time used: 17min
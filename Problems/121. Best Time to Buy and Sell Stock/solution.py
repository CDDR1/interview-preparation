class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0
        
        while r < len(prices):
            currProfit = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
                r += 1
                continue
            else:
                maxProfit = max(currProfit, maxProfit)
                r += 1
        
        return maxProfit
    
# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Sliding Window
# Time spent: 39min before looking at NeetCode's explanation
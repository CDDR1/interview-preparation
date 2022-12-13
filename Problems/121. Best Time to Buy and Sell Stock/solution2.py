class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                currProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, currProfit)
        return maxProfit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            minBuy = min(minBuy, prices[i])
            maxProfit = max(prices[i] - minBuy, maxProfit)
        return maxProfit
        #WCRT: O(N) | Space: O(1)
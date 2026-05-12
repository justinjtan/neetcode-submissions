class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] < minBuy:
                minBuy = prices[i]
            else:
                maxProfit = max(prices[i] - minBuy, maxProfit)
        return maxProfit
        #WCRT: O(N) | Space: O(1)
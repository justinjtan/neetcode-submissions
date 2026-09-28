class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        INF = float("inf")
        res = 0
        min_seen = INF
        for i in range(len(prices)):
            if prices[i] < min_seen:
                min_seen = prices[i]
            res = max(res, prices[i] - min_seen)
        
        return res
        #WCRT: O(N) | Space: O(1)
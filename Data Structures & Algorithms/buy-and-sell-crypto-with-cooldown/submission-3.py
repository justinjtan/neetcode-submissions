class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(len(prices) + 3)]

        for i in range(len(prices) - 1, -1, -1):
            dp[i] = dp[i + 1]
            for j in range(len(prices) - 1, i, -1):
                dp[i] = max(dp[i], prices[j] - prices[i] + dp[j + 2])
        
        return dp[0]
        #WCRT: O(N^2) | Space: O(N)
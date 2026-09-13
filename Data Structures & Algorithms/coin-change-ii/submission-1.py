class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(ct, start_idx):
            if ct == 0:
                return 1
            if ct < 0:
                return 0
            if (ct, start_idx) in memo:
                return memo[(ct, start_idx)]
            res = 0
            for i in range(start_idx, len(coins)): 
                memo[(ct - coins[i], i)] = dfs(ct - coins[i], i)
                res += memo[(ct - coins[i], i)]
            memo[(ct, start_idx)] = res
            return res

        return dfs(amount, 0)
        #WCRT: O(N * A) | Space: O(N * A) where N is length of coins and A is amount
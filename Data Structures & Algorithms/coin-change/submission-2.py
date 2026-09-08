class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")
        min_coins_by_amount = {}
        tmp = -1

        def dfs(money_held):
            nonlocal tmp
            if min_coins_by_amount.get(money_held, False):
                return min_coins_by_amount[money_held]
            if money_held < 0:
                min_coins_by_amount[money_held] = -1
            elif money_held == 0:
                min_coins_by_amount[money_held] = 0
            else: #money_held > 0
                for coin in coins:
                    tmp = dfs(money_held - coin)
                    if tmp == -1:
                        min_coins_by_amount[money_held - coin] = -1
                        continue
                    tmp += 1
                    min_coins_by_amount[money_held] = min(min_coins_by_amount.get(money_held, INF), tmp)
            return min_coins_by_amount.get(money_held, -1)
    
        return dfs(amount)
        #WCRT: O(N) | Space: O(N)
class Solution:
    def climbStairs(self, n: int) -> int:

        def dp(steps: int, memo: List[int]):
            if steps == n:
                return 1
            elif steps > n:
                return 0
            if memo[steps] != -1:
                return memo[steps]
            memo[steps] = dp(steps + 1, memo) + dp(steps + 2, memo)
            return memo[steps]

        return dp(0, [-1] * n)
        #WCRT: O(N) | Space: O(N)
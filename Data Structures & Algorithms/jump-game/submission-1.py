class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def dfs(i):
            if i == len(nums) - 1:
                return True
            if i in memo:
                return memo[i]
            for j in range(1, nums[i] + 1):
                memo[i + j] = dfs(i + j)
                if memo[i + j]:
                    return True
            memo[i] = False
            return False

        return dfs(0)
        #WCRT: O(N) | Space: O(N)
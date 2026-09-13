class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dfs(i, ct):
            if i >= len(nums):
                if ct == target:
                    return 1
                return 0
            if (i, ct) in memo:
                return memo[(i, ct)]
            memo[(i, ct)] = dfs(i + 1, ct + nums[i]) + dfs(i + 1, ct - nums[i])
            return memo[(i, ct)]
        
        return dfs(0, 0)
        #WCRT: O(N * A) | Space: O(N * A) where A is the max sum of nums 
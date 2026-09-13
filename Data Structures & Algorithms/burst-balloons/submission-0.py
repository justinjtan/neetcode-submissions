class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        new_nums = [1] + nums + [1]
        memo = {}
        
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            res = 0
            for i in range(l, r + 1):
                res = max(res, new_nums[l - 1] * new_nums[i] * new_nums[r + 1] + dfs(l, i - 1) + dfs(i + 1, r))
            memo[(l, r)] = res
            return res
        
        return dfs(1, len(nums))
        #WCRT: O(N^2) | Space: O(N^2)
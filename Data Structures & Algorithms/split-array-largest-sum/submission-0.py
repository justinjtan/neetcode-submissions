class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        memo = {}
        
        def dfs(i, k):
            if k == 1:
                return sum(nums[i:])
            if (i, k) in memo:
                return memo[(i, k)]
            res = float("inf")
            for j in range(i, len(nums) - (k - 1)):
                cur = max(sum(nums[i:j + 1]), dfs(j + 1, k - 1))
                res = min(res, cur)
            memo[(i, k)] = res
            return res
        
        return dfs(0, k)
        #WCRT: O(N * K) | Space: O(N * K)
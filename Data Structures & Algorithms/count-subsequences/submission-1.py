from functools import cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @cache
        def dfs(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            res = 0
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            res += dfs(i + 1, j)
            print(i, j, res)
            return res
        
        return dfs(0, 0)
            
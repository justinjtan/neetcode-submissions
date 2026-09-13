class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dfs(i, j):
            if j == len(p):
                return (i == len(s))
            if (i, j) in memo:
                return memo[(i, j)]
            res = False
            if j < len(p) - 1 and p[j + 1] == '*':
                res = dfs(i, j + 2)
                if i < len(s) and (p[j] == '.' or s[i] == p[j]):
                    res = res or dfs(i + 1, j) or dfs(i + 1, j + 2)
            if i < len(s) and j < len(p) and (s[i] == p[j] or p[j] == '.'):
                res = res or dfs(i + 1, j + 1)
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)
        #WCRT: O(N * M) | Space: O(N * M) where N is length of S and M is length of p.
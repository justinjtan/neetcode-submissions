class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        memo = {}
        
        def dfs(i):
            if i == len(s) - 1:
                return True
            if i >= len(s):
                return False
            if s[i] == '1':
                return False
            if i in memo:
                return memo[i]
            res = False
            for j in range(maxJump, minJump - 1, -1):
                memo[(i + j)] = dfs(i + j)
                res = res or memo[(i + j)]
                if res:
                    return True
            memo[i] = res
            return res

        return dfs(0)
        #WCRT: O(N) | Space: O(N)
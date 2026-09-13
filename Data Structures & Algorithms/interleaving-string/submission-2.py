class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}  
        
        def dfs(i, j, k):
            if k >= len(s3):
                if i >= len(s1) and j >= len(s2):
                    return True
                return False
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                memo[(i + 1, j, k + 1)] = dfs(i + 1, j, k + 1)
                res = memo[(i + 1, j, k + 1)]
            if j < len(s2) and s2[j] == s3[k]:
                memo[(i, j + 1, k + 1)] = dfs(i, j + 1, k + 1)
                res = res or memo[(i, j + 1, k + 1)]
            return res
        
        return dfs(0, 0, 0)
        #WCRT: O(A * B * C) | Space: O(A * B * C) where A, B, C is length of s1, s2, s3 respectively.
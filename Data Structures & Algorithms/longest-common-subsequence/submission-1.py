class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text1))] for _ in range(len(text2))]

        def dfs(i, j): #i is idx of text1 and j is idx of text2
            if i >= len(text1) or j >= len(text2):
                return 0
            if dp[j][i] != -1:
                return dp[j][i]
            if text1[i] == text2[j]:
                dp[j][i] = 1 + dfs(i + 1, j + 1)
            else:
                dp[j][i] = max(dfs(i + 1, j), dfs(i, j + 1))
            return dp[j][i]
        
        return dfs(0, 0)
        #WCRT: O(N * M) | Space: O(N * M) where N is length of text1 and M is length of text2
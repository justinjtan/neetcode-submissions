class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len, res_left, res_right = 0, -1, -1
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i + 1 <= 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if max_len < j - i + 1:
                        max_len = j - i + 1
                        res_left, res_right = i, j
        return s[res_left : res_right + 1]
        #WCRT: O(N^2) | Space: O(N^2)
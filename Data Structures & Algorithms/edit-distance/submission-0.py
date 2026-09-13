class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        
        def dfs(i, j):
            if i >= len(word1) and j >= len(word2):
                return 0
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            memo[(i, j)] = min(1 + dfs(i, j + 1), 1 + dfs(i + 1, j), 1 + dfs(i + 1, j + 1))
            return memo[(i, j)]
        
        return dfs(0, 0)
        #WCRT: O(N * M) | Space: O(N * M) where N is length of word1 and M is length of word2.
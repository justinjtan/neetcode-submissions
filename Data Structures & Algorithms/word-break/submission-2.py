class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo = {}

        def dfs(l, r):
            if l in memo:
                return memo[l]
            if r >= len(s):
                memo[l] = (l == r)
            elif s[l:r + 1] in word_set:
                memo[l] = dfs(r + 1, r + 1) or dfs(l, r + 1)
            else:
                memo[l] = dfs(l, r + 1)
            return memo[l]
        
        return dfs(0, 0)
        #WCRT: O(N^2 * W) | Space: O(N^2 * W) where W is the length of wordDict.
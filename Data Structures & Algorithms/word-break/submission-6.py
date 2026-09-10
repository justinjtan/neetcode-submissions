class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        t = 0
        for word in wordDict:
            t = max(t, len(word))
        memo = {}

        def dfs(l):
            if l in memo:
                return memo[l]
            if l >= len(s):
                memo[l] = True
                return True
            for i in range(min(len(s) - l, t)):
                if s[l:l + i + 1] in word_set:
                    if dfs(l + i + 1):
                        memo[l] = True
                        return True
            memo[l] = False
            return False
        
        return dfs(0)
        #WCRT: O((n * t^2) + m) | Space: O(n + (m * t)) where n is the length of the string, m length of wordDict and t is the max length of any word in wordDict.
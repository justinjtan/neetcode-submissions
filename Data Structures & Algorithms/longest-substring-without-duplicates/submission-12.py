class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = {}
        l = 0
        for r in range(len(s)):
            if s[r] in seen and l <= seen[s[r]]:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            res = max(res, r - l + 1)
        return res
        #WCRT: O(N) | Space: O(M) where M is the number of unique chars.
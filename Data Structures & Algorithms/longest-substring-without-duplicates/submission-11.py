class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = set()
        l = 0
        for r in range(len(s)):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res
        #WCRT: O(N) | Space: O(M) where M is the number of unique chars.
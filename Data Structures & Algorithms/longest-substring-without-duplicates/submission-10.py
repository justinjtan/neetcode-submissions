class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(s)):
            if s[right] in char_index and left <= char_index[s[right]] < right:
                left = char_index[s[right]] + 1
            char_index[s[right]] = right
            res = max(res, right - left + 1)
        return res
        #WCRT: O(N) | Space: O(M)
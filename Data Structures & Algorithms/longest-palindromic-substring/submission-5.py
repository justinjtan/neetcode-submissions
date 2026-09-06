class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len, left, right = 0, -1, -1
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            ct = (r - 1) - (l + 1) + 1
            if ct > max_len:
                max_len = ct
                left, right = l + 1, r - 1
            l, r = i, i
            if i + 1 < len(s) and s[i + 1] == s[i]:
                r = i + 1
            else:
                continue
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            ct = (r - 1) - (l + 1) + 1
            if ct > max_len:
                max_len = ct
                left, right = l + 1, r - 1
        return s[left:right + 1]
        #WCRT: O(N^2) | Space: O(1)
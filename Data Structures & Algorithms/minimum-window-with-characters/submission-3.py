class Solution:
    def isValid(self, s: dict, t: dict) -> bool:
        for char in t:
            if s[char] < t[char]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        t_char_count = defaultdict(int)
        s_char_count = defaultdict(int)
        for char in t:
            t_char_count[char] += 1
        l = 0
        min_curr = 100001
        window = (-1, -1)
        for r in range(len(s)):
            if s[r] in t_char_count:
                s_char_count[s[r]] += 1
            while self.isValid(s_char_count, t_char_count):
                if s[l] in t_char_count:
                    s_char_count[s[l]] -= 1
                if r - l + 1 < min_curr:
                    min_curr = r - l + 1
                    window = (l, r)
                l += 1
        return s[window[0]: window[1] + 1]
        #WCRT: O(N + M) | Space: O(K) where N is length of s and M is length of t and K is unique characters in t.
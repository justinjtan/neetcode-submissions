class Solution:
    def chars_in_string(self, counts_t: dict, counts_s: dict) -> bool:
        for char, ct in counts_t.items():
            if counts_s[char] < counts_t[char]:
                return False
        return True
        #WCRT: O(m) | Space: O(1) where m is the number of unique chars in counts_t.

    def minWindow(self, s: str, t: str) -> str:
        INF = float("inf")
        counts_t = Counter(t)
        counts_s = defaultdict(int)
        min_len = INF
        res_l, res_r = -1, -1
        l = 0
        for r in range(len(s)):
            counts_s[s[r]] += 1
            while self.chars_in_string(counts_t, counts_s):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res_l, res_r = l, r
                counts_s[s[l]] -= 1
                l += 1
            
        return s[res_l: res_r + 1]
        #WCRT: O(N * M) | Space: O(M) extra space and O(N) for output space where M is the number of unique chars in s and t.
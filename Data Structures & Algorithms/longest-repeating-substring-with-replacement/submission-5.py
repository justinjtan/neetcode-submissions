class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            while max(counts.values()) + k < r - l + 1:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        #WCRT: O(N) | Space: O(M) where M is the num of unique chars.
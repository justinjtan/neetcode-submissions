class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_s1 = Counter(s1)
        counts_s2 = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            counts_s2[s2[r]] += 1
            if r - l + 1 > len(s1):
                counts_s2[s2[l]] -= 1
                if counts_s2[s2[l]] == 0:
                    del counts_s2[s2[l]]
                l += 1
            if counts_s1 == counts_s2:
                return True
        return False
        #WCRT: O(N * M) | Space: O(M) where M is the number of unique characters in s1 & s2.
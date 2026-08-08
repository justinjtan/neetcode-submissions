class Solution:
    def createHashMap(self, s: str) -> dict:
        res = defaultdict(int)
        for char in s:
            res[char] += 1
        return res
        #WCRT: O(N) | Space: O(1)

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char_count = self.createHashMap(s1)
        s2_char_count = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            char = s2[r]
            if len(s1) < r - l + 1:
                s2_char_count[s2[l]] -= 1
                if s2_char_count[s2[l]] == 0:
                    del s2_char_count[s2[l]]
                l += 1
            if char in s1_char_count:
                s2_char_count[char] += 1
                if len(s1_char_count) == len(s2_char_count) and s1_char_count == s2_char_count:
                    return True
            else:
                l = r + 1
                if len(s2_char_count) != 0:
                    s2_char_count = defaultdict(int)
        return False
        #WCRT: O(N + M*N) | Space: O(N)    
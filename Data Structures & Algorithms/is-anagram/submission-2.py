class Solution:
    def createHashMap(self, s: str) -> dict:
        res = defaultdict(int)
        for char in s:
            res[char] += 1
        return res

    def isAnagram(self, s: str, t: str) -> bool:
        str_s = self.createHashMap(s)
        str_t = self.createHashMap(t)
        return str_s == str_t
        #WCRT: O(N) | Space: O(N)
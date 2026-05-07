class Solution:
    def findCharCount(self, hashMap: dict, s: str) -> None:
        for char in s:
            if char in hashMap:
                hashMap[char] += 1
            else:
                hashMap[char] = 1

    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        self.findCharCount(hashMap, s)
        for char in t:
            if char not in hashMap:
                return False
            hashMap[char] -= 1
        for value in hashMap.values():
            if value != 0:
                return False
        return True
    #WCRT: O(N) | Space: O(N)

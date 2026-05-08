class Solution:
    #Key Idea: Iterating through each string, creating a hashmap and compare it to the first/representative element of each of the previous hashmap groups
    #hashMap= str : count
    def findCharCount(self, hashMap: dict, string: str) -> None:
        for char in string:
            if char in hashMap:
                hashMap[char] += 1
            else:
                hashMap[char] = 1

    def isAnagram(self, hashMap1: dict, hashMap2: dict) -> bool:
        if len(hashMap1) != len(hashMap2):
            return False
        for key in hashMap1:
            if hashMap1[key] != hashMap2.get(key, 0):
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramArray = []
        hashArray = []
        for string in strs:
            foundGroup = False
            hashMap = {}
            self.findCharCount(hashMap, string)
            for idx in range(len(hashArray)):
                rep = hashArray[idx][0]
                if self.isAnagram(hashMap, rep):
                    hashArray[idx].append(hashMap)
                    anagramArray[idx].append(string)
                    foundGroup = True
                    break
            if not foundGroup:
                hashArray.append([hashMap])
                anagramArray.append([string])
        return anagramArray
    #WCRT: O(N*M) where M is the size of the largest string in the element
    #Space: O(N*M) where M is the size of the largest string in the element
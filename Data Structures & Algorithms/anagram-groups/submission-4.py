class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            charList = [0] * 26
            for char in string:
                charList[ord(char) - ord('a')] += 1
            res[tuple(charList)].append(string)
        return list(res.values())
        #WCRT: O(N * M) | Space: O(N * M) where M is the largest length of a string in strs
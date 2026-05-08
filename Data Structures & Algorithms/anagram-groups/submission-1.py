class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramHashMap = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            anagramHashMap[tuple(count)].append(string)
        return list(anagramHashMap.values())
    #WCRT: O(N*M)
    #Space: O(N)
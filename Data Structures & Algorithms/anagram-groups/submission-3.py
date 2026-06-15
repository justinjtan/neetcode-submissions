class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            sortedString = "".join(sorted(string))
            res[sortedString].append(string)
        return list(res.values())
        #WCRT: O(N * MLogM) | Space: O(N * M) where M is the largest length of a string in strs
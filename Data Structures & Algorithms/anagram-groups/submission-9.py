class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            anagrams["".join(sorted(s))].append(s)
        return list(anagrams.values())
        #WCRT: O(N * M log M) | Space: O(N * M) where N is length of strs and M is longest string in strs.
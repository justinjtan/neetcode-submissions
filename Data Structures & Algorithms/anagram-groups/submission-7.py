class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            anagrams["".join(sorted(s))].append(s)
        return [[val for val in anagrams[key]] for key in anagrams]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for char in s:
                key[ord(char) - ord('a')] += 1
            anagrams[tuple(key)].append(s)
        return list(anagrams.values())
        #WCRT: O(N * M) | Space: O(N * M) where N is length of strs and M is length of longest string in strs.
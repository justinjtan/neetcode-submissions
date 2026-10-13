class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        for i in range(len(min(strs, key=len))):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return "".join(prefix)
            prefix.append(strs[0][i])
        return "".join(prefix)
        #WCRT: O(N * M) | Space: O(M) where N is length of strs and M is the length of the longest common prefix.
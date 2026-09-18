class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        i = 0
        min_word_len = len(min(strs, key=len))
        equal = True

        while i < min_word_len and equal:
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    equal = False
                    break
            if equal:
                i += 1
        i -= 1
        if i < 0:
            return ""
        return strs[0][:i + 1]
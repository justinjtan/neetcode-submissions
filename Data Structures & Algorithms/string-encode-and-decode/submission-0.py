class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += string
            res += '.'
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        curr = ""
        for char in s:
            if char == ".":
                res.append(curr)
                curr = ""
            else:
                curr += char
        return res
    #WCRT: O(N) | Space: O(N)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_lookup = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        stack = []

        def solve(i):
            if i == len(digits):
                res.append("".join(stack))
                return
            for char in digits_lookup[digits[i]]:
                stack.append(char)
                solve(i + 1)
                stack.pop()
            return
        if len(digits) == 0:
            return res
        solve(0)
        return res
        #WCRT: O(N * 4^N) | Space: O(N) extra space and O(4^N) for output list
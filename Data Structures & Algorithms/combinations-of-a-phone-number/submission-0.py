class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_lookup = [(2, "abc"), (3,"def"), (4,"ghi"), (5,"jkl"), (6,"mno"), (7,"pqrs"), (8,"tuv"), (9,"wxyz")]
        res = []
        stack = []

        def solve(i):
            if i == len(digits):
                res.append("".join(stack))
                return
            for digit in digits_lookup:
                if str(digit[0]) == digits[i]:
                    for char in digit[1]:
                        stack.append(char)
                        solve(i + 1)
                        stack.pop()
                    return
        if len(digits) == 0:
            return res
        solve(0)
        return res
        #WCRT: O(N * 4^N) | Space: O(N) extra space and O(4^N) for output list
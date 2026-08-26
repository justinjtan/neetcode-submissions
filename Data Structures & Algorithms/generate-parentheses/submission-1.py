class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def solve(open_ct, close_needed):
            if len(stack) == (n * 2):
                res.append("".join(stack))
                return
            if open_ct < n:
                stack.append('(')
                solve(open_ct + 1, close_needed + 1)
                stack.pop()
            if close_needed > 0:
                stack.append(')')
                solve(open_ct, close_needed - 1)
                stack.pop()
        
        solve(0, 0)
        return res
        #WCRT: O(N * 2^N) | Space: O(N) extra space and O(2^N) for output list
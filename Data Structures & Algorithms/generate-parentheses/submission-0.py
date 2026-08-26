class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def solve(open_ct, close_needed, curr):
            if len(curr) == (n * 2):
                res.append(curr)
                return
            if open_ct < n:
                solve(open_ct + 1, close_needed + 1, curr + '(')
            if close_needed > 0:
                solve(open_ct, close_needed - 1, curr + ')')
        
        solve(0, 0, "")
        return res
        #WCRT: O(N * 2^N) | Space: O(N) extra space and O(2^N) for output list
class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        stack = []

        def solve(i, curr):
            if i == len(s):
                if not curr:
                    res.append(stack.copy())
                return
            curr.append(s[i])
            if self.isPalindrome(curr):
                stack.append("".join(curr))
                solve(i + 1, [])
                stack.pop()
            solve(i + 1, curr)
            curr.pop()

        solve(0, [])
        return res
        #WCRT: O(N * 2^N) | Space: O(N) extra space and O(2^N) for output list
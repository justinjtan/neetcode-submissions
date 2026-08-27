class Solution:
    def isPalindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        stack = []

        def solve(i, j):
            if j >= len(s):
                if i == j:
                    res.append(stack.copy())
                return
            if self.isPalindrome(s, i, j):
                stack.append(s[i:j + 1])
                solve(j + 1, j + 1)
                stack.pop()
            solve(i, j + 1)

        solve(0, 0)
        return res
        #WCRT: O(N * 2^N) | Space: O(N) extra space and O(2^N) for output list
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev_2, prev_1 = 1, 2
        for i in range(3, n + 1):
            curr = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = curr
        return curr
        #WCRT: O(N) | Space: O(1)
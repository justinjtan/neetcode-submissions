class Solution:

    def can_combine(self, c1: str, c2: str) -> bool:
        if c1 == '1':
            return True
        elif c1 == '2':
            return c2 != '7' and c2 != '8' and c2 != '9'
        return False

    def numDecodings(self, s: str) -> int:
        next_2, next_1 = 1, 1
        for i in range(len(s) - 1, -1, -1):
            curr = next_1
            if i + 1 < len(s) and self.can_combine(s[i], s[i + 1]):
                curr += next_2
            if s[i] == '0':
                curr = 0
            next_2 = next_1
            next_1 = curr
        return curr
        #WCRT: O(N) | Space: O(1)
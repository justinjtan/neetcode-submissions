class Solution:

    def can_combine(self, c1: str, c2: str) -> bool:
        if c1 == '1':
            return True
        elif c1 == '2':
            return c2 != '7' and c2 != '8' and c2 != '9'
        return False

    def numDecodings(self, s: str) -> int:
        combinations = {}

        def dfs(i):
            if i >= len(s):
                return 1
            elif s[i] == '0':
                return 0
            elif combinations.get(i, False):
                return combinations[i]
            else:
                combinations[i] = dfs(i + 1)
                if i + 1 < len(s) and self.can_combine(s[i], s[i + 1]):
                    combinations[i] += dfs(i + 2)
                return combinations[i]

        for i in range(len(s) - 1, -1, -1):
            dfs(i)
        return combinations.get(0, 0)
        #WCRT: O(N) | Space: O(N)
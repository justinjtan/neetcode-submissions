class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_open = []
        stack_wildcard = []
        for i in range(len(s)):
            if s[i] == '(':
                stack_open.append(i)
            elif s[i] == '*':
                stack_wildcard.append(i)
            else:
                if stack_open:
                    stack_open.pop()
                elif stack_wildcard:
                    stack_wildcard.pop()
                else:
                    return False
        while stack_open and stack_wildcard:
            idx_open = stack_open.pop()
            idx_wildcard = stack_wildcard.pop()
            if idx_open > idx_wildcard:
                return False
        return not stack_open
        #WCRT: O(N) | Space: O(N)
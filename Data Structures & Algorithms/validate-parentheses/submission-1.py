class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_chars = ['(', '{', '[']
        close_chars = [')', '}', ']']
        for char in s:
            if char in open_chars:
                stack.append(char)
            elif len(stack) == 0:
                return False
            else:
                top = stack.pop()
                for idx in range(len(close_chars)):
                    if char == close_chars[idx] and top != open_chars[idx]:
                        return False
        return len(stack) == 0
        #WCRT : O(N) | Space: O(N)
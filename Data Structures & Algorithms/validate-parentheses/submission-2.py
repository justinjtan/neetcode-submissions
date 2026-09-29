class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        stack = []
        for char in s:
            if char in close_to_open:
                if not stack or stack[-1] != close_to_open[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack
        #WCRT: O(N) | Space: O(N)
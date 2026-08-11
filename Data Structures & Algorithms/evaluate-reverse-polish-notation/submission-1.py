class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            temp = 0
            if char.lstrip('-').isnumeric():
                stack.append(int(char))
                continue
            elif char == '+':
                temp = stack[-1] + stack[-2]
            elif char == '*':
                temp = stack[-1] * stack[-2]
            elif char == '-':
                temp = stack[-2] - stack[-1]
            else:
                temp = int(stack[-2] / stack[-1])
            stack.pop()
            stack[-1] = temp
        return stack[0]
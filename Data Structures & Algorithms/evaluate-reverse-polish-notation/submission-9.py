class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif char == "*":
                val = stack.pop() * stack.pop()
                stack.append(val)
            elif char == "-":
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(first_num - second_num)
            elif char == "/":
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(math.trunc(first_num / second_num))
            else:
                stack.append(int(char))
        return stack[0]
        #WCRT: O(N) | Space: O(N)
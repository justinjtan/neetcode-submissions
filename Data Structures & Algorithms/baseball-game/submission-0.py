class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for char in operations:
            if char == "+":
                new_num = stack[-1] + stack[-2]
                stack.append(new_num)
            elif char == "C":
                stack.pop()
            elif char == "D":
                new_num = stack[-1] * 2
                stack.append(new_num)
            else:
                stack.append(int(char))
        return sum(stack)
        #WCRT: O(N) | Space: O(N)
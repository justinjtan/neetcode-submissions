class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "]":
                curr = deque([])
                print(stack)
                while not stack[-1].isnumeric():
                    curr.appendleft(stack.pop())
                repeated = int(stack.pop())
                res_str = "".join(curr)
                for j in range(repeated):
                    stack.append(res_str)
                i += 1
            elif s[i] == "[":
                i += 1
            elif s[i].isnumeric():
                curr = [s[i]]
                i += 1
                while i < len(s) and s[i].isnumeric():
                    curr.append(s[i])
                    i += 1
                stack.append("".join(curr))
            else:
                stack.append(s[i])
                i += 1
        return "".join(stack)
        #WCRT: O(N * M) | Space: O(N * M) where N is length of s and M is the largest k in s.
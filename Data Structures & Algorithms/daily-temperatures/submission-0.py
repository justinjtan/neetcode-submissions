class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for idx in range(len(temperatures)):
            while stack and temperatures[idx] > stack[-1][0]:
                res[stack[-1][1]] = idx - stack[-1][1]
                stack.pop()
            stack.append((temperatures[idx], idx))
        return res
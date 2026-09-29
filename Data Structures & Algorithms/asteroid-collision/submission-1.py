class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for size in asteroids:
            if size > 0:
                stack.append(size)
            else:
                while stack and abs(size) > stack[-1] and stack[-1] > 0:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(size)
                elif stack[-1] > 0 and stack[-1] == abs(size):
                    stack.pop()
        return stack
        #WCRT: O(N) | Space: O(N)
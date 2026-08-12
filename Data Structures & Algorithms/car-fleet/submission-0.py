class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for idx in range(len(position)):
            time_to_target = (target - position[idx]) / speed[idx]
            stack.append((position[idx], time_to_target))
        stack.sort()
        res = 1
        base = stack.pop()
        while stack:
            car = stack.pop()
            if base[1] < car[1]:
                res += 1
                base = car
        return res
        #WCRT: O(NlogN) | Space: O(N)
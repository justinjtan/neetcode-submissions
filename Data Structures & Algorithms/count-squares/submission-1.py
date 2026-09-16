class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point
        for x, y in self.points:
            if x != qx and abs(x - qx) == abs(y - qy):
                res += self.points[(x, y)] * self.points.get((x, qy), 0) * self.points.get((qx, y), 0)
        
        return res
        #WCRT: O(N) | Space: O(N)

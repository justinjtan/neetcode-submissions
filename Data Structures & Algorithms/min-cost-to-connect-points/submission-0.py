class DSU:

    def __init__(self, n: int):
        self.components = n
        self.parents = list(range(n))
        self.size = [1] * n
    
    def find(self, point: int) -> int:
        if self.parents[point] != point:
            self.parents[point] = self.find(self.parents[point])
        return self.parents[point]

    def union(self, u: int, v: int) -> bool:
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.size[pu] += self.size[pv]
        self.parents[pv] = pu
        return True

class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(edges, [distance, i, j])
        
        dsu = DSU(len(points))
        res = 0
        while edges:
            distance, u, v = heapq.heappop(edges)
            if dsu.union(u, v):
                res += distance
        return res
        #WCRT: O(N^2 log N) | Space: O(N^2)
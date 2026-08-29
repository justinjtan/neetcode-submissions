class DSU:

    def __init__(self, n: int):
        self.components = n
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, node: int) -> int:
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, u: int, v: int) -> None:
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return
        self.components -= 1
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.size[pu] += self.size[pv]
        self.parents[pv] = pu

    def get_components(self) -> int:
        return self.components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)
        return dsu.get_components()
        #Time (Amortized worst case runtime): O(V + m * A(V)) | Space: O(V) where m is the number of find and union operations and A is the ackermann function.
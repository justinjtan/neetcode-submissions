class DSU:

    def __init__(self, n: int):
        self.components = n
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, node: int) -> int:
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, u: int, v: int) -> bool:
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        self.components -= 1
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.size[pu] += self.size[pv]
        self.parents[pv] = pu
        return True
    
    def get_components(self) -> int:
        return self.components

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        return dsu.components == 1
        #WCRT: O(V + E) | Space: O(V + E)
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        
        def dfs(u):
            visited.add(u)
            res = 0
            for v in adj[u]:
                if v not in visited:
                    res += dfs(v)
            print(u, res)
            return 2 + res if hasApple[u] or res > 0 else res
        
        return max(dfs(0) - 2, 0)
        #WCRT: O(V * E) | Space: O(V + E)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = {i: [] for i in range(n)}
        for node1, node2 in edges:
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)
        visited = set()
        curr = 0

        def dfs(last):
            nonlocal curr
            if curr in visited:
                return False
            visited.add(curr)
            for nei in neighbors[curr]:
                if nei == last:
                    continue
                temp = curr
                curr = nei
                if not dfs(temp):
                    return False
                curr = temp
            return True
        
        res = dfs(-1)
        if not res:
            return False
        return len(visited) == n
        #WCRT: O(V + E) | Space: O(V + E)
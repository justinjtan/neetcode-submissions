class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for src, dst, time in times:
            adj[src].append([dst, time])
        min_heap = [[0, k]]
        visited = set()
        time = 0
        while min_heap:
            t1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            time = t1
            for n2, t2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, [t2 + t1, n2])
        return time if len(visited) == n else -1
        #WCRT: O(E log V) | Space: O(V + E)
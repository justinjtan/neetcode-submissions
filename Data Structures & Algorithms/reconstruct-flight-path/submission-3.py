class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)
        res = deque([])

        def dfs(airport):
            while adj[airport]:
                smallest = heapq.heappop(adj[airport])
                dfs(smallest)
            res.appendleft(airport)

        dfs("JFK")
        return list(res)
        # WCRT: O(E log E) | Space: O(V + E)
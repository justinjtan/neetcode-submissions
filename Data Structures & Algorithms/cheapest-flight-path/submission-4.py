class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inf = float("inf")
        adj = {i: [] for i in range(n)}
        for dep, arr, price in flights:
            adj[dep].append([price, arr])

        queue = [[0, -1, src]] # price, num of stops, airport
        visited = {}
        while queue:
            price, num_of_stops, airport = heapq.heappop(queue)
            if airport == dst:
                return price
            visited[airport] = num_of_stops
            for nei in adj[airport]:
                if num_of_stops < k and num_of_stops + 1 < visited.get(nei[1], inf):
                    heapq.heappush(queue, [nei[0] + price, num_of_stops + 1, nei[1]])
        return -1
        #WCRT: O(E log V) | Space: O(E + V)
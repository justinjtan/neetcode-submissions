class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for src, dst, time in times:
            adj[src].append([dst, time])
        
        min_time = [float("inf") for _ in range(n + 1)]

        def dfs(curr, time):
            if time >= min_time[curr]:
                return
            min_time[curr] = time
            for dst, time_to_dst in adj[curr]:
                dfs(dst, time + time_to_dst)
        
        dfs(k, 0)
        res = float("-inf")
        for i in range(1, n + 1):
            if min_time[i] == float("inf"):
                return -1
            res = max(res, min_time[i])
        return res
        #WCRT: O(V * E) | Space: O(V + E)
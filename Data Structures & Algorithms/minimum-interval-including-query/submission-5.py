class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        INF = float("inf")
        min_len_interval = {}
        intervals.sort()
        queries_copy = queries.copy()
        queries.sort()
        min_heap = []

        i, q = 0, 0 #i is pointer for intervals and q is pointer for queries
        while i < len(intervals) and q < len(queries):
            start = intervals[i][0]
            end = intervals[i][1]
            if queries[q] >= start:
                heapq.heappush(min_heap, (end - start + 1, intervals[i]))
                i += 1
            elif not min_heap:
                q += 1
            else:
                while min_heap:
                    interval = min_heap[0][1]
                    len_interval = min_heap[0][0]
                    if interval[1] >= queries[q]:
                        min_len_interval[queries[q]] = len_interval
                        q += 1
                        break
                    heapq.heappop(min_heap)
                continue
        
        while min_heap and q < len(queries):
            interval = min_heap[0][1]
            len_interval = min_heap[0][0]
            if queries[q] <= interval[1]:
                min_len_interval[queries[q]] = len_interval
                q += 1
                continue
            heapq.heappop(min_heap)

        res = []
        for query in queries_copy:
            res.append(min_len_interval.get(query, -1))
        
        return res
        #WCRT: O(N log N + M log M) | Space: O(N + M) where N is length of intervals and M is length of queries.
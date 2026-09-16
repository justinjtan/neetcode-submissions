class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))
        res = []

        while max_heap:
            ct, char = heapq.heappop(max_heap)
            if len(res) >= 2 and char == res[-1] and char == res[-2]:
                if not max_heap:
                    break
                ct2, char2 = heapq.heappop(max_heap)
                res.append(char2)
                ct2 += 1
                if ct2 < 0:
                    heapq.heappush(max_heap, (ct2, char2))
                heapq.heappush(max_heap, (ct, char))
            else:
                res.append(char)
                ct += 1
                if ct < 0:
                    heapq.heappush(max_heap, (ct, char))
        
        return "".join(res)
        #WCRT: O(A + B + C) | Space: O(1) extra space O(A + B + C) for output space
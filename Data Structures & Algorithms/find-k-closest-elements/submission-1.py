class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        for i in range(len(arr)):
            diff = abs(x - arr[i])
            heapq.heappush(max_heap, (-diff, -i))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        res = []
        while max_heap:
            _, i = heapq.heappop(max_heap)
            res.append(arr[-i])
        res.sort()
        return res
        #WCRT: O(N log N) | Space: O(k)
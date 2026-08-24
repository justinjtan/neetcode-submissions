class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-weight for weight in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            stone_a = -heapq.heappop(max_heap)
            stone_b = -heapq.heappop(max_heap)
            diff = stone_a - stone_b #since stone_a >= stone_b in max heap
            if diff != 0:
                heapq.heappush(max_heap, -diff)
        if max_heap:
            return -max_heap[0]
        return 0
        #WCRT: O(N log N) | Space: O(N)
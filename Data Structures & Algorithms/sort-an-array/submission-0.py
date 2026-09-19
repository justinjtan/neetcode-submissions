class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        max_heap = []
        queue = deque([])

        for num in nums:
            heapq.heappush(max_heap, -num)
        
        while max_heap:
            queue.appendleft(-heapq.heappop(max_heap))
        
        return list(queue)
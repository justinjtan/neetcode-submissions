class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = Counter(nums)
        max_heap = []

        for key, val in nums_freq.items():
            heapq.heappush(max_heap, (-val, key))
        
        res = []
        while k > 0:
            res.append(heapq.heappop(max_heap)[1])
            k -= 1
        
        return res
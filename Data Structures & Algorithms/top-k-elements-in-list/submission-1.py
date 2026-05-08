class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        min_heap = []
        for key, count in hashMap.items():
            heapq.heappush(min_heap, (count, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        res = []
        for ct, n in min_heap:
            res.append(n)
        return res
        #WCRT: O(Nlogk) | Space: O(N+k)
        
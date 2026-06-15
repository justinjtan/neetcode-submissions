class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctMap = defaultdict(int)
        for num in nums:
            ctMap[num] += 1
        min_heap = []
        for key in ctMap.keys():
            heapq.heappush(min_heap, (ctMap[key], key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        res = []
        for numTuple in min_heap:
            res.append(numTuple[1])
        return res
        #WCRT: O(Nlogk) | Space: O(N + k)
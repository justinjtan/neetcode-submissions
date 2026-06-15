class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctMap = defaultdict(int)
        for num in nums:
            ctMap[num] += 1
        ctMapSorted = dict(sorted(ctMap.items(), key=lambda item: item[1], reverse=True))
        res = []
        for key in ctMapSorted.keys():
            if k == 0:
                return res
            res.append(key)
            k -= 1
        return res
        #WCRT: O(NlogN) | Space: O(N)
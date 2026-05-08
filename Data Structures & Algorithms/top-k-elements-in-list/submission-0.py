class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashCount = defaultdict(int)
        for num in nums:
            hashCount[num] += 1
        newHashCount = dict(sorted(hashCount.items(), key=lambda item: item[1]))
        res = []
        for key in reversed(newHashCount):
            if k == 0:
                return res
            res.append(key)
            k -= 1
        return res
        #WCRT: O(NlogN) | Space: O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqByIndex = [[] for _ in range(len(nums) + 1)]
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        for key, count in hashMap.items():
            freqByIndex[count].append(key)
        res = []
        for lst in reversed(freqByIndex):
            for n in lst:
                if len(res) == k:
                    return res
                res.append(n)
        return res
        #WCRT: O(N) | Space: O(N)
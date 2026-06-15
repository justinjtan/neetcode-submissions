class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = defaultdict(int)
        for num in nums:
            numMap[num] += 1
        freqMap = defaultdict(list)
        for key, value in numMap.items():
            freqMap[value].append(key)
        res = []
        for i in range(len(nums), 0, -1):
            for num in freqMap[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
        #WCRT: O(N) | Space: O(N)
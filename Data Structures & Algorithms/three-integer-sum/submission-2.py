class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combinationMap = defaultdict(list)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums), 1):
                add = nums[i] + nums[j]
                combinationMap[add].append([i, j])
        res = []
        traversedNum = set()
        for i in range(len(nums)):
            if nums[i] not in traversedNum and combinationMap.get(-nums[i], 0) != 0:
                traversedNum.add(nums[i])
                for idxList in combinationMap[-nums[i]]:
                    if i not in idxList:
                        zeroSum = [nums[i], nums[idxList[0]], nums[idxList[1]]]
                        zeroSum.sort()
                        if zeroSum not in res:
                            res.append(zeroSum)
        return res
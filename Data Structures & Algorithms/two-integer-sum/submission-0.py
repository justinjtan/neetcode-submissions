class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #key,value = num,idx
        for idx in range(len(nums)):
            difference = target - nums[idx]
            if difference in hashMap:
                return [hashMap[difference], idx]
            hashMap[nums[idx]] = idx
        #WCRT: O(N) | Space: O(N)
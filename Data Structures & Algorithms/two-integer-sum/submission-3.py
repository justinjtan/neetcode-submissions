class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_freq = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_freq:
                return [nums_freq[target - nums[i]], i]
            nums_freq[nums[i]] = i
        return -1
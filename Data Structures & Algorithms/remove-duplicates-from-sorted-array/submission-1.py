class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        unique_nums.sort()
        for i in range(len(unique_nums)):
            nums[i] = unique_nums[i]
        return len(unique_nums)
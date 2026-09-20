class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for i in range(1, 10000000):
            if i not in nums_set:
                return i
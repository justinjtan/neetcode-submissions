class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = ((1 + len(nums)) * len(nums)) // 2
        return expected_sum - sum(nums)
        #WCRT: O(N) | Space: O(1)
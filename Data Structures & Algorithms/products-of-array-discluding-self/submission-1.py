class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        suff = [1] * len(nums)
        for idx in range(1, len(nums), 1):
            pref[idx] = pref[idx - 1] * nums[idx - 1]
        for idx in range(len(nums) - 2, -1, -1):
            suff[idx] = suff[idx + 1] * nums[idx + 1]
        for idx in range(len(nums)):
            nums[idx] = pref[idx] * suff[idx]
        return nums
        #WCRT: O(N) | Space: O(N)
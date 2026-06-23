class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [[] for _ in range(len(nums))]
        suff = [[] for _ in range(len(nums))]
        res = []
        pref[0] = 1
        suff[len(nums) - 1] = 1
        for i in range(1, len(nums)):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(len(nums)):
            res.append(pref[i] * suff[i])
        return res
        #WCRT: O(N) | Space: O(N)

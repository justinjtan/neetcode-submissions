class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        res = nums[len(nums)-k:len(nums)] + nums[:len(nums)-k]
        for i in range(len(nums)):
            nums[i] = res[i]
        #WCRT: O(N) | Space: O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = 0
        res = float("-inf")

        for num in nums:
            cur_max = max(global_max + num, num)
            global_max = cur_max
            res = max(res, cur_max)
        
        return res
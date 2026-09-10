class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        res = 1

        for i in range(len(nums) - 1, -1, -1):
            cur_max = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    cur_max = max(cur_max, 1 + memo[j])
            memo[i] = cur_max
            res = max(res, cur_max)
        
        return res
        #WCRT: O(N^2) | Space: O(N)
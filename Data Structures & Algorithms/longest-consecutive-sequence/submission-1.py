class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        res = 1
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] - 1 == nums[i - 1]:
                cur += 1
            else:
                cur = 1
            res = max(cur, res)
        
        return res

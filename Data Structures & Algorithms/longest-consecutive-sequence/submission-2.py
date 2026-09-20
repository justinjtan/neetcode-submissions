class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for num in nums:
            if (num - 1) not in nums_set:
                cur = 1
                while (num + cur) in nums_set:
                    cur += 1
                res = max(res, cur)
        
        return res

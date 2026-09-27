class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue
                if r < len(nums) - 1 and nums[r] == nums[r + 1]:
                    r -= 1
                    continue
                if nums[l] + nums[r] == -nums[i]:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                else:
                    l += 1
        
        return res
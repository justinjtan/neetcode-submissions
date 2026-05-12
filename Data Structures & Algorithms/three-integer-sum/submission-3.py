class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, val in enumerate(nums):
            if val > 0:
                break
            if i > 0 and val == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = val + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
        #WCRT: O(N^2) | Space: O(1)
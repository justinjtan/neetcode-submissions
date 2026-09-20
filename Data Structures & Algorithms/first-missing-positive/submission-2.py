class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            v = abs(nums[i]) - 1
            print(v)
            if 0 <= v < len(nums):
                if nums[v] > 0:
                    nums[v] = -nums[v]
                else:
                    nums[v] = -abs(nums[i])
        
        print(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1
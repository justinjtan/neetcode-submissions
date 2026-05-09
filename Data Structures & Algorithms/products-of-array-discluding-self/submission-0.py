class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsSum = 1
        zeroExist = False
        secondZeroExist = False
        for num in nums:
            if num == 0 and zeroExist:
                secondZeroExist = True
            elif num == 0:
                zeroExist = True
            else:
                numsSum *= num
        for idx in range(len(nums)):
            if nums[idx] != 0 and zeroExist:
                nums[idx] = 0
            elif nums[idx] == 0:
                if secondZeroExist:
                    nums[idx] = 0
                else:
                    nums[idx] = numsSum
            else:
                nums[idx] = numsSum // nums[idx]
        return nums
        #WCRT: O(N) | Space: O(N)
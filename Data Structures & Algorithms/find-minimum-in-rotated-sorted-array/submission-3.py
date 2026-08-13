class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] > nums[right]:
            while right - left > 1:
                middle = (left + right) // 2
                if nums[middle] < nums[left]:
                    right = middle
                else:
                    left = middle
            return nums[right]
        return nums[left]
        #WCRT: O(log n)| Space: O(1)
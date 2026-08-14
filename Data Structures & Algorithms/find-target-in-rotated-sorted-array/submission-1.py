class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] >= nums[left]:
                if nums[left] <= target <= nums[middle]:
                    right = middle
                    continue
                left = middle + 1
            else:
                if nums[right] >= target >= nums[middle]:
                    left = middle
                    continue
                right = middle - 1
        return -1
        #WCRT: O(log n) | Space: O(1)
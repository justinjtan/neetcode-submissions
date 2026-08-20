class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_idx = nums[0]
        fast_idx = nums[0]
        fast_idx = nums[fast_idx]
        while slow_idx != fast_idx:
            slow_idx = nums[slow_idx]
            fast_idx = nums[fast_idx]
            fast_idx = nums[fast_idx]
        fast_idx = 0
        while slow_idx != fast_idx:
            slow_idx = nums[slow_idx]
            fast_idx = nums[fast_idx]
        return slow_idx
        #WCRT: O(N) | Space: O(1)
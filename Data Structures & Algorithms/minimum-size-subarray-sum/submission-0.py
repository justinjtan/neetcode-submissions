class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF = float("inf")
        res = INF
        l = 0
        curr_count = 0
        for r in range(len(nums)):
            curr_count += nums[r]
            while curr_count >= target:
                res = min(res, r - l + 1)
                curr_count -= nums[l]
                l += 1
        return res if res != INF else 0
        #WCRT: O(N) | Space: O(1)
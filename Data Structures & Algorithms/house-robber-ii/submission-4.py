class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        def dfs(start, end):
            prev_2, prev_1 = 0, 0
            for i in range(start, end):
                curr = max(nums[i] + prev_2, prev_1)
                prev_2 = prev_1
                prev_1 = curr
            return curr

        return max(dfs(1, len(nums)), dfs(0, len(nums) - 1))
        #WCRT: O(N) | Space: O(1)
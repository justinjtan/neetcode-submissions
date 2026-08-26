class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def solve(idx, curr):
            if idx >= len(nums):
                res.append(curr)
                return
            solve(idx + 1, curr + [nums[idx]])
            i = idx
            while idx < len(nums) and nums[idx] == nums[i]:
                idx += 1
            solve(idx, curr)

        solve(0, [])
        return res
        #WCRT: O(N * 2^N) | Space: O(N) extra space and O(N * 2^N) for output list
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def solve(nums, curr, idx, can_append):
            nonlocal res
            if can_append:
                res.append(curr)
            if idx >= len(nums):
                return
            solve(nums, curr + [nums[idx]], idx + 1, True)
            solve(nums, curr[:], idx + 1, False)
        
        solve(nums, [], 0, True)
        return res
        #WCRT: O(N * N!) | Space: (2^N)
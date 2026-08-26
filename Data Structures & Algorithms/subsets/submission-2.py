class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def solve(nums, curr, idx):
            nonlocal res
            if idx >= len(nums):
                res.append(curr)
                return
            solve(nums, curr + [nums[idx]], idx + 1)
            solve(nums, curr[:], idx + 1)
        
        solve(nums, [], 0)
        return res
        #WCRT: O(N * 2^N) | Space: O(N) extra space O(2^N) output list
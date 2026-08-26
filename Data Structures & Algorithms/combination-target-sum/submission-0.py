class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def solve(ct, curr, idx):
            nonlocal res
            if ct >= target or idx >= len(nums):
                if ct == target:
                    res.append(curr)
                return
            else:
                temp_ct = 0
                temp_curr = []
                while temp_ct <= target:
                    solve(ct + temp_ct, curr + temp_curr, idx + 1)
                    temp_ct += nums[idx]
                    temp_curr.append(nums[idx])
            
        solve(0, [], 0)
        return res
        #WCRT: O(target/min(nums) * N) | Space: O(N) extra space and O(target/min(nums) * N) for output list
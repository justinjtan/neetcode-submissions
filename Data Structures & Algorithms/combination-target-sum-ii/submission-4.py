class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def solve(ct, curr, idx, took_prev):
            if ct >= target or idx >= len(candidates):
                if ct == target:
                    res.append(curr)
                return
            elif idx > 0 and candidates[idx] == candidates[idx - 1]: #duplicate
                solve(ct, curr, idx + 1, False)
                if took_prev:
                    solve(ct + candidates[idx], curr + [candidates[idx]], idx + 1, True)
                return
            solve(ct + candidates[idx], curr + [candidates[idx]], idx + 1, True)
            solve(ct, curr, idx + 1, False)

        solve(0, [], 0, True)
        return res
        #WCRT: O(N * 2^N) | Space: O(N) extra space and O(2^N) for output list
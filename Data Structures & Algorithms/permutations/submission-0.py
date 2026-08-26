class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
        
        def solve(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for num in list(nums_dict):
                curr.append(num)
                del nums_dict[num]
                solve(curr)
                curr.pop()
                nums_dict[num] += 1
        
        solve([])
        return res
        #WCRT: O(N!) | Space: O(N) extra space and O(N!) for output list
                

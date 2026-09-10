class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2
        visited = set()

        def dfs(ct):
            if ct == 0:
                return True
            if ct < 0:
                return False
            if ct in memo:
                return memo[ct]
            for i in range(len(nums)):
                if i in visited:
                    continue
                visited.add(i)
                if dfs(ct - nums[i]):
                    return True
                visited.remove(i)
                memo[ct - nums[i]] = False
            return False

        return dfs(target)
        #WCRT: O(N * M) | Space: O(N * M) where N is length of nums and M is the max value of an element in nums.
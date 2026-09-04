class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])
        prev_2, prev_1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            curr = min(prev_2, prev_1) + cost[i]
            prev_2 = prev_1
            prev_1 = curr
        return min(curr, prev_2)
        #WCRT: O(N) | Space: O(1)
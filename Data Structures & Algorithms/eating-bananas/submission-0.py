import math

class Solution:
    def hoursRemaining(self, piles: List[int], h: int, k: int) -> int:
        for pile in piles:
            h -= math.ceil(pile / k)
        return h
        #WCRT: O(N) | Space: O(1)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float("inf")
        lower_bound = math.ceil(sum(piles) / h)
        upper_bound = max(piles)
        while lower_bound <= upper_bound:
            middle = (lower_bound + upper_bound) // 2
            hours_remaining = self.hoursRemaining(piles, h, middle)
            if hours_remaining >= 0:
                res = min(res, middle)
                upper_bound = middle - 1
            else:
                lower_bound = middle + 1
        return res
        #WCRT: O(N log M) | Space: O(1)

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l, r = 0, len(people) - 1
        while l <= r:
            weight = people[l] + people[r]
            r -= 1
            if weight <= limit:
                l += 1
            res += 1
        
        return res
        #WCRT: O(N log N) | Space: O(1)
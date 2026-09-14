class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        target_exist = [False] * 3
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                if a == target[0]:
                    target_exist[0] = True
                if b == target[1]:
                    target_exist[1] = True
                if c == target[2]:
                    target_exist[2] = True
        return target_exist == [True] * 3
        #WCRT: O(N) | Space: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,1
        for i in range(l, len(numbers)):
            r = l + 1
            for j in range(r, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        #WCRT: O(N^2) | Space: O(1)
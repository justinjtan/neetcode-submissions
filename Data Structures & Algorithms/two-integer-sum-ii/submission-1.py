class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx = 0
        for i in range(idx, len(numbers)):
            for j in range(idx + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        #WCRT: O(N^2) | Space: O(1)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums
        #WCRT: O(N) | Space: O(1) extra space and O(N) for the output.
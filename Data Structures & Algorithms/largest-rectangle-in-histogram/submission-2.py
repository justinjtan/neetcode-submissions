class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        left = [-1] * len(heights)
        right = [len(heights)] * len(heights)
        for idx in range(1, len(heights)):
            i = idx - 1
            while i >= 0 and heights[idx] <= heights[i]:
                i = left[i]
            left[idx] = i
        for idx in range(len(heights) -2, -1, -1):
            i = idx + 1
            while i < len(heights) and heights[idx] <= heights[i]:
                i = right[i]
            right[idx] = i
        for idx in range(len(heights)):
            curr_width = right[idx] - left[idx] - 1
            curr_area = heights[idx] * curr_width
            res = max(res, curr_area)
        return res
        #WCRT: O(N) | Space: O(N)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = -1
        l,r = 0, len(heights) - 1
        while l < r:
            ct = (r - l) * min(heights[r], heights[l])
            maxArea = max(ct, maxArea)
            if heights[l] > heights[r]:
                r_ptr = heights[r]
                r -= 1
                while l < r and heights[r] < r_ptr:
                    r -= 1
            elif heights[l] < heights[r]:
                l_ptr = heights[l]
                l += 1
                while l < r and heights[l] < l_ptr:
                    l += 1
            else:
                l_ptr = heights[l]
                l += 1
                while l < r and heights[l] < l_ptr:
                    l += 1
        return maxArea
        #WCRT: O(N) | Space: O(1)

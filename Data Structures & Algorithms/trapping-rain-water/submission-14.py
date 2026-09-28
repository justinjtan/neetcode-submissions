class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        while l < r:
            if height[l] >= height[r]:
                r -= 1
                if height[r] > max_right:
                    max_right = height[r]
                res += max_right - height[r]
            else:
                l += 1
                if height[l] > max_left:
                    max_left = height[l]
                res += max_left - height[l]
        return res
        #WCRT: O(N) | Space: O(1)

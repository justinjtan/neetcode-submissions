class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, res, l_max, r_max = 0, len(height) - 1, 0, 0, 0
        while l != r:
            if height[l] <= height[r]:
                l_max = max(l_max, height[l])
                l += 1
                if height[l] < l_max:
                    res += l_max - height[l]
            else:
                r_max = max(r_max, height[r])
                r -= 1
                if height[r] < r_max:
                    res += r_max - height[r]
        return res
        #WCRT: O(N) | Space: O(1)
            

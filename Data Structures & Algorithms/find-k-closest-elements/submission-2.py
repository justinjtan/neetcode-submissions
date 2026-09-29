class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l + 1 > k:
            diff_l, diff_r = abs(x - arr[l]), abs(x - arr[r])
            if diff_l > diff_r:
                l += 1
            else:
                r -= 1
        
        return arr[l:r+1]
        #WCRT: O(N) | Space: O(1) extra space and O(K) for the output space.
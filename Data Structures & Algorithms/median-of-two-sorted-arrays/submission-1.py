class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            shorter_list, longer_list = nums1, nums2
        else:
            shorter_list, longer_list = nums2, nums1
        half = (len(shorter_list) + len(longer_list)) // 2
        left, right = 0, len(shorter_list)
        while left <= right:
            middle_shorter = (left + right) // 2
            middle_larger = half - middle_shorter
            shorter_left = shorter_list[middle_shorter - 1] if middle_shorter > 0 else float('-inf')
            shorter_right = shorter_list[middle_shorter] if middle_shorter < len(shorter_list) else float('inf')
            larger_left = longer_list[middle_larger - 1] if middle_larger > 0 else float('-inf')
            larger_right = longer_list[middle_larger] if middle_larger < len(longer_list) else float('inf')
            if shorter_left <= larger_right and larger_left <= shorter_right:
                if (len(shorter_list) + len(longer_list)) % 2 == 0:
                    return (max(shorter_left, larger_left) + min(shorter_right, larger_right)) / 2.0
                else:
                    return min(shorter_right, larger_right)
            elif shorter_left > larger_right:
                right = middle_shorter - 1
            else:
                left = middle_shorter + 1
        #WCRT: O(log(min(n,m))) | Space: O(1)
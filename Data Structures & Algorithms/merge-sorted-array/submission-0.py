class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                tmp1 = nums1[i]
                nums1[i] = nums2[j]
                j += 1
                m += 1
                for k in range(i + 1, m):
                    tmp2 = nums1[k]
                    nums1[k] = tmp1
                    tmp1 = tmp2
            i += 1
        
        for k in range(m, len(nums1)):
            nums1[k] = nums2[j]
            j += 1
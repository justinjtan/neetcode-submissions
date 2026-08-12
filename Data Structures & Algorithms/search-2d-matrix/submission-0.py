class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            middle = (left + right) // 2
            lower_bound = matrix[middle][0]
            upper_bound = matrix[middle][-1]
            if lower_bound <= target <= upper_bound:
                lst = matrix[middle]
                left = 0
                right = len(lst) - 1
                while left <= right:
                    middle = (left + right) // 2
                    if target == lst[middle]:
                        return True
                    elif target > lst[middle]:
                        left = middle + 1
                    else:
                        right = middle - 1
                return False
            elif target > upper_bound:
                left = middle + 1
            else:
                right = middle - 1
        return False
        #WCRT: O(log(M * N)) | Space: O(1)
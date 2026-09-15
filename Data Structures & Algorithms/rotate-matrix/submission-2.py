class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            m = n - (i * 2) - 1
            base = n - 1 - i
            print(m)
            for j in range(m):
                start = [i, i + j]
                print(f"start: {start}")
                directions = [[start[1], base], [base, base - j], [base - j, i], [i, start[1]]]
                print(f"directions: {directions}")
                next_num = matrix[start[0]][start[1]]
                for dr, dc in directions:
                    print(f"swapping to {(dr, dc)}")
                    tmp = matrix[dr][dc]
                    matrix[dr][dc] = next_num
                    next_num = tmp
            print(f"moving to the next layer")
            print(matrix)
        #WCRT: O(N^2) | Space: O(1)
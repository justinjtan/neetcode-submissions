class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW, COL = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * (COL + 1) for _ in range(ROW + 1)]

        for r in range(1, ROW + 1):
            for c in range(1, COL + 1):
                self.sum_matrix[r][c] = matrix[r - 1][c - 1] + self.sum_matrix[r][c - 1] + self.sum_matrix[r - 1][c] - self.sum_matrix[r - 1][c - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_matrix[row2 + 1][col2 + 1] - self.sum_matrix[row2 + 1][col1] - self.sum_matrix[row1][col2 + 1] + self.sum_matrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
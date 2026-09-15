class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW, COL = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for r in range(ROW):
            if r in zero_rows:
                for c in range(COL):
                    matrix[r][c] = 0
        
        for c in range(COL):
            if c in zero_cols:
                for r in range(ROW):
                    matrix[r][c] = 0
        #WCRT: O(M * N) Space: O(M + N)
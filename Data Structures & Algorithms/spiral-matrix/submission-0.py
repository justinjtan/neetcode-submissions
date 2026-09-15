class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROW, COL = len(matrix), len(matrix[0])
        up_bound, right_bound, bottom_bound, left_bound = 0, COL - 1, ROW - 1, 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        res = []
        r, c = 0, 0
        i, j = directions[2]

        while len(res) != (ROW * COL):
            res.append(matrix[r][c])
            if r + i < up_bound:
                i, j = directions[2]
                r += i
                c += j
                left_bound += 1
                continue
            elif r + i > bottom_bound:
                i, j = directions[3]
                r += i
                c += j
                right_bound -= 1
                continue
            elif c + j > right_bound:
                i, j = directions[1]
                r += i
                c += j
                up_bound += 1
                continue
            elif c + j < left_bound:
                i, j = directions[0]
                r += i
                c += j
                bottom_bound -= 1
                continue
            r += i
            c += j
        
        return res
        #WCRT: O(M * N) | Space: O(1)
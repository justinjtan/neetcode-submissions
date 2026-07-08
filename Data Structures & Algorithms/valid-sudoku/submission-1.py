class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            numCount = defaultdict(int)
            for j in range(9):
                if board[i][j] != '.':
                    if numCount[board[i][j]] >= 1:
                        return False
                    numCount[board[i][j]] += 1
        for i in range(9):
            numCount = defaultdict(int)
            for j in range(9):
                if board[j][i] != '.':
                    if numCount[board[j][i]] >= 1:
                        return False
                    numCount[board[j][i]] += 1
        coords = [(0, 0), (3, 0), (6, 0), (0, 3), (3, 3), (6, 3), (0, 6), (3, 6), (6, 6)]
        for a,b in coords:
            numCount = defaultdict(int)
            for i in range(3):
                for j in range(3):
                    if board[a][b] != '.':
                        if numCount[board[a][b]] >= 1:
                            return False
                        numCount[board[a][b]] += 1
                    b += 1
                a += 1
                b -= 3
        return True
        #WCRT: O(N^2) | Space: O(N)
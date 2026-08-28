class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROW, COL = len(board), len(board[0])
        non_surrounded_cells = set()
        has_visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or board[r][c] == 'X' or (r, c) in non_surrounded_cells:
                return
            non_surrounded_cells.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for c in range(COL):
            dfs(0, c)
            dfs(ROW - 1, c)
        for r in range(ROW):
            dfs(r, 0)
            dfs(r, COL - 1)
        for r in range(ROW):
            for c in range(COL):
                if (r, c) not in non_surrounded_cells:
                    board[r][c] = 'X'
        #WCRT: O(N * M) | Space: O(N * M)
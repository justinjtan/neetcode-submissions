class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        ROW, COL = len(grid), len(grid[0])
        res = 0
        ct = 0

        def dfs(r, c):
            nonlocal ct
            if r < 0 or c < 0 or r >= ROW or c >= COL:
                return
            if grid[r][c] == 1:
                grid[r][c] = 0
                ct += 1
                for dr, dc in directions:
                    dfs(r + dr, c + dc)
            
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    dfs(r, c)
                    res = max(res, ct)
                    ct = 0
        return res
        #WCRT: O(R * C) | Space: O(R * C)
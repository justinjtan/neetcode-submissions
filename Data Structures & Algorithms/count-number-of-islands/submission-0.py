class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        res = 0
        has_visited = set()

        def dfs(x, y):
            if x < 0 or y < 0 or x >= COL or y >= ROW:
                return
            if grid[y][x] == "1" and (x, y) not in has_visited:
                has_visited.add((x, y))
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
        
        for y in range(ROW):
            for x in range(COL):
                if grid[y][x] == "1" and (x, y) not in has_visited:
                    res += 1
                    dfs(x, y)
        return res
        #WCRT: O(N * M) | Space: O(N * M) where N is number of rows and M is number of columns
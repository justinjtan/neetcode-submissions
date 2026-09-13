class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        ROW, COL = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(COL)] for _ in range(ROW)]
        visited = set()

        def dfs(r, c, prev):
            if r < 0 or c < 0 or r >= ROW or c >= COL or (r, c) in visited or prev >= matrix[r][c]:
                return 0
            if dp[r][c] != 0:
                return dp[r][c]
            visited.add((r, c))
            for dr, dc in directions:
                dp[r][c] = max(dp[r][c], 1 + dfs(r + dr, c + dc, matrix[r][c]))
            visited.remove((r, c))
            return dp[r][c]
        
        res = 0
        for r in range(ROW):
            for c in range(COL):
                visited = set()
                res = max(res, dfs(r, c, float("-inf")))
        return res
        #WCRT: O(N^2) | Space: O(N^2)
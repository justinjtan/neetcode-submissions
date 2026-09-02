class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        if ROW == 1 and COL == 1:
            return 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set()
        queue = [[grid[0][0], 0, 0]] #time, r, c
        while queue:
            time, r, c = heapq.heappop(queue)
            if r == ROW - 1 and c == COL - 1:
                return time
            for dr, dc in directions:
                r2 = r + dr
                c2 = c + dc
                if 0 <= r2 < ROW and 0 <= c2 < COL and (r2, c2) not in visited:
                    visited.add((r2, c2))
                    heapq.heappush(queue, [max(grid[r2][c2], time), r2, c2])
        return -1       
        #WCRT: O(N^2 log N) | Space: O(N^2)  
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        ROW, COL = len(grid), len(grid[0])
        res = -1
        rotten_fruit = []

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    rotten_fruit.append((r, c))
        queue = deque(rotten_fruit)

        if not queue:
            res += 1
        
        def add_rotten(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] != 1:
                return
            grid[r][c] = 2
            queue.append((r, c))
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    add_rotten(r + dr, c + dc)
            res += 1

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    return -1
        return res
        #WCRT: O(N * M) | Space: O(N * M)
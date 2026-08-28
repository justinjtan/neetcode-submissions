class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        ROW, COL = len(grid), len(grid[0])
        chest_location = []
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    chest_location.append((r, c))
        initial_queue = []
        for r, c in chest_location:
            for dr, dc in directions:
                initial_queue.append([r + dr, c + dc])
        queue = deque(initial_queue)
        distance = 1
        while queue:
            for i in range(len(queue)):
                r1, c1 = queue.popleft()
                if r1 < 0 or c1 < 0 or r1 >= ROW or c1 >= COL:
                    continue
                if grid[r1][c1] == 2147483647:
                    grid[r1][c1] = distance
                    for dr, dc in directions:
                        queue.append([r1 + dr, c1 + dc])
            distance += 1
        #WCRT: O(N * M) | Space: O(N * M)
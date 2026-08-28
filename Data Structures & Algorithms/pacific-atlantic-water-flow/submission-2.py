class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        ROW, COL = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        res = []
        
        def dfs(r, c, last_height, reachable_sea):
            if r < 0 or c < 0 or r >= ROW or c >= COL or (r, c) in reachable_sea or heights[r][c] < last_height:
                return
            reachable_sea.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], reachable_sea)
        
        #move from the borders to inwards
        for c in range(COL):
            dfs(0, c, float("-inf"), pacific)
            dfs(ROW - 1, c, float("-inf"), atlantic)
        for r in range(ROW):
            dfs(r, 0, float("-inf"), pacific)
            dfs(r, COL - 1, float("-inf"), atlantic)
        for r in range(ROW):
            for c in range(COL):
                coord = (r, c)
                if coord in pacific and coord in atlantic:
                    res.append([r, c])
        return res
        #WCRT: O(N * M) | Space: O(N * M)
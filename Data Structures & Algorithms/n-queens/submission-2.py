class Solution:
    def compute_queen_range(self, x: int, y: int, add:int , n: int, in_queen_range: List[List[int]]):
        for i in range(n):
            in_queen_range[y][i] += add
            in_queen_range[i][x] += add
            if x + i < n:
                if y + i < n:
                    in_queen_range[y + i][x + i] += add
                if y - i >= 0:
                    in_queen_range[y - i][x + i] += add
            if x - i >= 0:
                if y - i >= 0:
                    in_queen_range[y - i][x - i] += add
                if y + i < n:
                    in_queen_range[y + i][x - i] += add

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        stack = []
        in_queen_range = []
        for i in range(n):
            curr = []
            stack_curr = []
            for j in range(n):
                curr.append(0)
                stack_curr.append('.')
            in_queen_range.append(curr)
            stack.append(stack_curr)

        def solve(y):
            if y == n:
                res.append([])
                for row in stack:
                    res[-1].append("".join(row))
                return
            for x in range(n):
                if not in_queen_range[y][x]:
                    stack[y][x] = 'Q'
                    self.compute_queen_range(x, y, 1, n, in_queen_range)
                    solve(y + 1)
                    self.compute_queen_range(x, y, -1, n, in_queen_range)
                    stack[y][x] = '.'
        
        solve(0)
        return res
        #WCRT: O(N * N!) | Space: O(N^2) extra space and O(N!) for output list
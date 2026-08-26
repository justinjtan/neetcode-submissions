class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        has_visited = []
        for _ in range(len(board)):
            curr = []
            for _ in range(len(board[0])):
                curr.append(False)
            has_visited.append(curr)

        def solve(x, y, i, has_started):
            nonlocal res
            if i == len(word):
                res = True
                return
            elif x >= len(board[0]) or x < 0 or y >= len(board) or y < 0 or has_visited[y][x]:
                return
            if board[y][x] == word[i]:
                has_visited[y][x] = True
                solve(x + 1, y, i + 1, True)
                solve(x - 1, y, i + 1, True)
                solve(x, y + 1, i + 1, True)
                solve(x, y - 1, i + 1, True)
                has_visited[y][x] = False
            if not has_started:
                solve((x + 1) % len(board[0]), y + (x + 1) // len(board[0]), i, False)

        solve(0, 0, 0, False)
        return res
        #WCRT: O(M^2 * N^2) | Space: O(1)
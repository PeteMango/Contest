from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        n, m = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != 'O':
                return
            board[i][j] = 'A'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(n):
            for j in [0, m-1]:
                dfs(i, j)
        for j in range(m):
            for i in [0, n-1]:
                dfs(i, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'

s = Solution()

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s.solve(board)

for row in board:
    print(row)

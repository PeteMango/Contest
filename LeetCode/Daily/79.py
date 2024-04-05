# Wed, April 3, 2024

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y, index):
            if index == len(word):
                return True

            if x < 0 or x >= n or y < 0 or y >= m or board[x][y] != word[index]:
                return False

            temp = board[x][y]
            board[x][y] = '!'

            for dx, dy in directions:
                if dfs(x + dx, y + dy, index + 1):
                    return True

            board[x][y] = temp
            return False

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True

        return False


s = Solution()

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

board = [["a"]]
word = "a"

print(s.exist(board, word))

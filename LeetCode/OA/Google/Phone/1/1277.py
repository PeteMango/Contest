from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        psa = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                psa[i][j] = matrix[i-1][j-1] + psa[i-1][j] + psa[i][j-1] - psa[i-1][j-1]
        ans = 0

        for i in range(n):
            for j in range(m):
                for k in range(1, min(n - i, m - j) + 1):
                    total = self.query(psa, i, j, k)
                    if total == k*k:
                        ans += 1
                    else:
                        break

        return ans

    def query(self, psa: List[List[int]], x, y, length: int) -> int:
        return psa[x + length][y + length] - psa[x][y + length] - psa[x + length][y] + psa[x][y]

s = Solution()

matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]

print(s.countSquares(matrix))

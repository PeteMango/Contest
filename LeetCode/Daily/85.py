from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        matrix = [[int(char) for char in row] for row in matrix]
        n, m = len(matrix), len(matrix[0])

        psa_matrix = [[0] * m for _ in range(n)]

        for j in range(m):
            for i in range(n):
                if matrix[i][j] == 1:
                    psa_matrix[i][j] = psa_matrix[i-1][j] + 1
                else:
                    psa_matrix[i][j] = 0

        def compute_sum(x, y: int) -> int:
            mx_sum, mn_showed = 0, 40005
            for j in range(y, -1, -1):
                if psa_matrix[x][y] == 0:
                    break
                mn_showed = min(mn_showed, psa_matrix[x][j])
                mx_sum = max(mx_sum, mn_showed * (y - j + 1))

            return mx_sum

        mx = 0
        for j in range(m-1, -1, -1):
            for i in range(n):
                if psa_matrix[i][j] > 0:
                    mx = max(mx, compute_sum(i, j))

        return mx

s = Solution()

matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

matrix = [["0"]]

matrix = [["1"]]

print(s.maximalRectangle(matrix))

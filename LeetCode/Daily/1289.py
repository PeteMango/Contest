# Fri, April 26, 2024

from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        def debug(dp: List[List[int]]) -> None:
            for i in range(len(dp)):
                print(dp[i])
            return

        n, m = len(grid), len(grid[0])
        dp = [[10**5+5 for _ in range(m)] for _ in range(n)]

        if n == 1:
            return min(grid[0])

        dp[0] = grid[0]

        for i in range(1, n):
            for j in range(m):
                for k in range(m):
                    if j != k:
                        dp[i][j] = min(dp[i-1][k], dp[i][j])
                dp[i][j] += grid[i][j]

        return min(dp[n-1])

s = Solution()

grid = [[1,2,3],[4,5,6],[7,8,9]]

grid = [[7]]

print(s.minFallingPathSum(grid))
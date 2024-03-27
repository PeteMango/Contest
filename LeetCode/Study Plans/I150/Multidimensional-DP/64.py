from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                pos = int(1e7 + 5)
                if i > 0:
                    pos = min(pos, dp[i-1][j])
                if j > 0:
                    pos = min(pos, dp[i][j-1])

                dp[i][j] += pos

        print(dp)
        return dp[-1][-1]

s = Solution()

grid = [[1,3,1],[1,5,1],[4,2,1]]

grid = [[1,2,3],[4,5,6]]

print(s.minPathSum(grid))

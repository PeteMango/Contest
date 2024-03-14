from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]

        dp[0][0] = 1

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]

        print(dp)
        return dp[-1][-1]

s = Solution()

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]

print(s.uniquePathsWithObstacles(obstacleGrid))

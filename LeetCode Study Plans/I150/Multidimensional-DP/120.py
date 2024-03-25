from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle
        for i in range(1, len(dp)):
            for j in range(len(dp[i])):
                dp[i][j] += min(dp[i-1][min(len(dp[i-1]) - 1, j)], dp[i-1][max(0, j-1)])

        # print(dp)
        mx = int(1e5 + 5)

        for i in range(len(dp[-1])):
            mx = min(dp[-1][i], mx)

        return mx

s = Solution()

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

triangle = [[-10]]

print(s.minimumTotal(triangle))

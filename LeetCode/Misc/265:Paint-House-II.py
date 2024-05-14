from typing import List

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        def printGrid(dp: List[List[int]]):
            for row in dp:
                print(row)
            print()

        n, m = len(costs), len(costs[0])
        dp = [[10**5-5 for i in range(m)] for j in range(n)]

        for i in range(m):
            dp[0][i] = costs[0][i]


        for i in range(1, n):
            prev_first = prev_second = 10**5 + 5
            prev_firstidx = prev_secondidx = -1

            for j in range(m):
                cost = dp[i-1][j]
                if cost < prev_first:
                    prev_second, prev_secondidx = prev_first, prev_firstidx
                    prev_first, prev_firstidx = cost, j
                elif cost < prev_second:
                    prev_second, prev_secondidx = cost, j

            for j in range(m):
                if j == prev_firstidx:
                    dp[i][j] = costs[i][j] + prev_second
                else:
                    dp[i][j] = costs[i][j] + prev_first

        return min(dp[n-1])

s = Solution()

costs = [[1,5,3],[2,9,4]]

costs = [[1,3],[2,4]]

costs = [
    [10,15,12,14,18,5],
    [5, 12,18,13,15,8],
    [4, 7, 4, 2, 10,18],
    [20,9, 9, 19,20,5],
    [10,15,10,15,16,20],
    [9,6,11,10,12,11],
    [7,10,6,12,20,8],
    [3,4,4,18,10,2]
]

print(s.minCostII(costs))

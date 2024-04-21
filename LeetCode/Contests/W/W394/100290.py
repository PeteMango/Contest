from collections import defaultdict
from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if n == 1:
            changes = 0
            for j in range(1, m):
                if grid[0][j] == grid[0][j-1]:
                    changes += 1
            return changes

        freq_list = []
        for col in range(m):
            freq_dict = defaultdict(int)
            for row in range(n):
                freq_dict[grid[row][col]] += 1
            freq_list.append(freq_dict)

        dp = [[float('inf')] * m for _ in range(m)]

        for value, count in freq_list[0].items():
            dp[value][0] = n - count

        for col in range(1, m):
            for value in range(m):
                if value in freq_list[col]:
                    for prev_value in range(m):
                        if prev_value in freq_list[col-1]:
                            if value != prev_value:
                                dp[value][col] = min(dp[value][col], dp[prev_value][col-1] + (n - freq_list[col][value]))

        min_ops = float('inf')
        for value in range(m):
            min_ops = min(min_ops, dp[value][m-1])

        return int(min_ops) if min_ops != float('inf') else -1

s = Solution()

grid = [[1,0,2],[1,0,2]]

grid = [[1,1,1],[0,0,0]]

grid = [[1],[2],[3]]

grid = [[3,5,3,6,0,9,9,2,3,3],[6,6,7,5,1,8,3,8,0,3]]

grid = [[2,6,6,9,8,4,2,6,2,3]]

grid = [[1,1,1], [1,1,1], [1,1,1]]

print(s.minimumOperations(grid))

from typing import List
from collections import defaultdict
from functools import cache

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        nums = [defaultdict(int) for _ in range(n)]

        for j in range(n):
            for i in range(m):
                nums[j][grid[i][j]] += 1

        @cache
        def move(i, value: int):
            if i == n:
                return 0

            num_changes = m - nums[i][value]
            return num_changes + min(move(i+1, new_val) for new_val in range(10) if new_val != value)

        return min(move(0, value) for vawlue in range(10))

s = Solution()

grid = [[1,0,2],[1,0,2]]

grid = [[1,1,1],[0,0,0]]

grid = [[1],[2],[3]]

grid = [[3,5,3,6,0,9,9,2,3,3],[6,6,7,5,1,8,3,8,0,3]]

grid = [[2,6,6,9,8,4,2,6,2,3]]

grid = [[1,1,1], [1,1,1], [1,1,1]]

print(s.minimumOperations(grid))

# Sun, May 12, 2024

from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        arr = [[0 for i in range(cols - 2)] for j in range(rows - 2)]

        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        for i in range(1, rows-1):
            for j in range(1, cols-1):
                arr[i-1][j-1] = grid[i][j]

                for dx, dy in directions:
                    arr[i-1][j-1] = max(arr[i-1][j-1], grid[i+dx][j+dy])

        return arr

s = Solution()

grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]

grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]

print(s.largestLocal(grid))

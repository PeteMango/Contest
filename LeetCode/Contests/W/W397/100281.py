from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        def debug(arr: List[List[int]]) -> None:
            for row in arr:
                print(row)
            return

        rows, cols = len(grid), len(grid[0])

        min_arr = [[0 for i in range(cols)] for j in range(rows)]
        min_arr[0][0] = grid[0][0]
        for i in range(1, rows):
            min_arr[i][0] = min(min_arr[i-1][0], grid[i][0])
        for j in range(1, cols):
            min_arr[0][j] = min(min_arr[0][j-1], grid[0][j])

        for i in range(1, rows):
            for j in range(1, cols):
                min_arr[i][j] = min(min_arr[i-1][j], min_arr[i][j-1], grid[i][j])

        ans = -10**5-5
        for i in range(rows):
            for j in range(cols):
                if i > 0:
                    ans = max(ans, grid[i][j] - min_arr[i-1][j])
                if j > 0:
                    ans = max(ans, grid[i][j] - min_arr[i][j-1])

        return ans

s = Solution()

grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]

# grid = [[4,3,2],[3,2,1]]

print(s.maxScore(grid))

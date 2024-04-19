from typing import

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        while True:
            location = self.check_island(grid)

            if location[0] == -1 and location[1] == -1:
                break

            self.remove_conencted(grid, location[0], location[1])
            cnt += 1

        return cnt

    def remove_conencted(self, grid:List[List[str]], i, j: int):
        if grid[i][j] == '0':
            return
        if grid[i][j] == '1':
            grid[i][j] = '0'

        if i > 0:
            self.remove_conencted(grid, i-1, j)
        if j > 0:
            self.remove_conencted(grid, i, j-1)
        if i < len(grid)-1:
            self.remove_conencted(grid, i+1, j)
        if j < len(grid[0])-1:
            self.remove_conencted(grid, i, j+1)


    def check_island(self, grid:List[List[str]]) -> tuple:
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    return (i, j)

        return (-1, -1)

s = Solution()

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(s.numIslands(grid))

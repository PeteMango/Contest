from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        psa = self.prefix_sum(grid)

        print(psa)

        cnt = 0

        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if psa[i][j] <= k:
                    cnt += 1

        return cnt

    def prefix_sum(self, arr: List[List[int]]) -> List[List[int]]:
        rows, cols = len(arr), len(arr[0])

        prefix_sum = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                prefix_sum[i][j] += arr[i][j]

                if i > 0:
                    prefix_sum[i][j] += prefix_sum[i-1][j]

                if j > 0:
                    prefix_sum[i][j] += prefix_sum[i][j-1]

                if i > 0 and j > 0:
                    prefix_sum[i][j] -= prefix_sum[i-1][j-1]

        return prefix_sum

s = Solution()

# grid = [[7,6,3],[6,6,1]]
# k = 18

grid = [[7,2,9],[1,5,0],[2,6,6]]
k = 20

print(s.countSubmatrices(grid, k))

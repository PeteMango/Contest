from typing import List

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        return min(self.check_operations(grid, 0), self.check_operations(grid, 1), self.check_operations(grid, 2))

    def check_operations(self, arr: List[List[int]], y_val: int) -> int:
        n = len(arr)

        cost_y = 0

        for i in range(int((n+1)/2)):
            # print(f'checking {arr[i][i]} {arr[i][n-i-1]}')
            if arr[i][i] != y_val:
                cost_y += 1

            if arr[i][n-i-1] != y_val:
                cost_y += 1

        if arr[int(n/2)][int(n/2)] != y_val:
            cost_y -= 1

        for i in range(int((n+1)/2), n):
            if arr[i][int(n/2)] != y_val:
                cost_y += 1


        if y_val == 0:
            # print(f'y_val: {y_val} not_y: {min(self.cost_not_y(arr, 1), self.cost_not_y(arr, 2))} y: {cost_y}')
            return min(self.cost_not_y(arr, 1), self.cost_not_y(arr, 2)) + cost_y
        elif y_val == 1:
            # print(f'y_val: {y_val} not_y: {min(self.cost_not_y(arr, 0), self.cost_not_y(arr, 2))} y: {cost_y}')
            return min(self.cost_not_y(arr, 0), self.cost_not_y(arr, 2)) + cost_y

        # print(f'y_val: {y_val} not_y: {min(self.cost_not_y(arr, 0), self.cost_not_y(arr, 1))} y: {cost_y}')
        return min(self.cost_not_y(arr, 0), self.cost_not_y(arr, 1)) + cost_y

    def cost_not_y(self, arr: List[List[int]], val: int) -> int:
        n = len(arr)

        cost_not_y = 0

        for i in range(int((n+1)/2)):
            for j in range(n):
                if j != i and j != n - i - 1 and arr[i][j] != val:
                    cost_not_y += 1

        for i in range(int((n+1)/2), n):
            for j in range(n):
                if j != int(n/2) and arr[i][j] != val:
                    cost_not_y += 1

        return cost_not_y

s = Solution()

grid = [[1,2,2],[1,1,0],[0,1,0]]

grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]

print(s.minimumOperationsToWriteY(grid))

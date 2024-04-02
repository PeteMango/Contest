from typing import List
from collections import deque

class Solution:
    def getMaximumGold(self, G: List[List[int]]) -> int:
        self.mx_money = 0
        n, m = len(G), len(G[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y, cur: int) -> None:
            money = G[x][y]
            cur += money

            self.mx_money = max(self.mx_money, cur)

            G[x][y] = 0
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if new_x >= 0 and new_x < len(G) and new_y >= 0 and new_y < len(G[0]) and G[new_x][new_y] != 0:
                    dfs(new_x, new_y, cur)

            G[x][y] = money

        for i in range(n):
            for j in range(m):
                dfs(i, j, 0)

        return self.mx_money

s = Solution()

grid = [[0,6,0],[5,8,7],[0,9,0]]

# grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]

print(s.getMaximumGold(grid))

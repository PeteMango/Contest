# Fri, April 19, 2024

from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        n, m = len(land), len(land[0])

        def update(land: List[List[int]], tx, ty, bx, by: int) -> None:
            for i in range(tx, bx+1):
                for j in range(ty, by+1):
                    land[i][j] = 0

        def printLand(land: List[List[int]]) -> None:
            for row in land:
                print(row)
            print()

        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    # printLand(land)
                    tx, ty = i, j
                    bx, by = 0, 0

                    for dx in range(i, n):
                        if land[dx][j] == 1:
                            bx = dx
                        else:
                            break

                    for dy in range(j, m):
                        if land[i][dy] == 1:
                            by = dy
                        else:
                            break
                    ans.append([tx, ty, bx, by])
                    update(land, tx, ty, bx, by)

        return ans

s = Solution()

land = [[1,0,0],[0,1,1],[0,1,1]]

land = [[1,1],[1,1]]

land = [[0]]

print(s.findFarmland(land))

from typing import List

class UnionFind:
    def __init__(self, m, n: int) -> int:
        self.parent = [i for i in range(m*n+1)]
        self.numisland = 0
    
    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x
        
        return self.find(self.parent[x])

    def union(self, a, b: int) -> None:
        aparent, bparent = self.find(a), self.find(b)
        
        # already connected islands
        if aparent == bparent:
            return
        
        self.parent[aparent] = bparent
        self.numisland -= 1

class Solution:
    def numIslands2(self, n: int, m: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(m, n)
        grid = [[0 for _ in range(m)] for _ in range(n)]
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        print(f'grid: {grid}')

        ans = []
        for r, c in positions:
            print(f'r, c: {r} {c}')
            if grid[r][c] == 1:
                ans.append(uf.numisland)
                continue
            
            grid[r][c] = 1
            uf.numisland += 1

            for dx, dy in dir:
                nx, ny = r+dx, c+dy
                if nx >= 0 and nx < n and ny < m and ny >= 0 and grid[nx][ny] == 1:
                    uf.union(r*m+c, nx*m+ny)
            
            ans.append(uf.numisland)

        # print(grid)
        return ans


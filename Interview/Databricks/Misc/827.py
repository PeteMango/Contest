class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, m, g = len(grid), len(grid[0]), []
        for row in grid:
            g.append(row.copy())
        
        if n == m == 1:
            return 1

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def label(x, y, lab: int):
            if x < 0 or y < 0 or x >= n or y >= m:
                return 0

            if g[x][y] != 1:
                return 0
            
            rest = 1
            g[x][y] = lab
            for dx, dy in direction:
                rest += label(x+dx, y+dy, lab)
            return rest

        size = g.copy()
        def tagsize(x, y, lab, sz: int):
            if x < 0 or y < 0 or x >= n or y >= m:
                return

            if g[x][y] != lab:
                return
            
            size[x][y] = (lab, sz)
            for dx, dy in direction:
                tagsize(x+dx, y+dy, lab, sz)
 
        index = 2
        for i in range(n):
            for j in range(m):
                if g[i][j] == 1:
                    sz = label(i, j, index)
                    tagsize(i, j, index, sz)
                    index += 1

        for i in range(n):
            for j in range(m):
                if size[i][j] == 0:
                    size[i][j] = (0, 0)

        max_size = 0
        for i in range(n):
            for j in range(m):
                if size[i][j][0] == 0:
                    gain = defaultdict(int)
                    if i > 0:
                        gain[size[i-1][j][0]] = size[i-1][j][1]
                    if i < n - 1:
                        gain[size[i+1][j][0]] = size[i+1][j][1]
                    if j > 0:
                        gain[size[i][j-1][0]] = size[i][j-1][1]
                    if j < m - 1:
                        gain[size[i][j+1][0]] = size[i][j+1][1]

                    tot = 0
                    for k, v in gain.items():
                        tot += v
                    max_size = max(max_size, tot + 1)

        for i in range(n):
            for j in range(m):
                if size[i][j][1] > max_size:
                    max_size = size[i][j][1]
                       
        return max_size
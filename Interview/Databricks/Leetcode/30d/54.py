class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m, x, y, idx = len(matrix), len(matrix[0]), 0, 0, 0
        if n == m and m == 1:
            return [1]
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # E, S, W, N
        ret = []

        def inside(x, y):
            return x < n and x >= 0 and y < m and y >= 0
        
        while True:
            print(x, y)
            ret.append(matrix[x][y])
            matrix[x][y] = -105

            nx, ny = x + dir[idx][0], y + dir[idx][1]
            if not inside(nx, ny) or matrix[nx][ny] == -105:
                idx = (idx + 1) % 4
            else:
                x, y = nx, ny
                continue
            
            nx, ny = x + dir[idx][0], y + dir[idx][1]
            if not inside(nx, ny) or matrix[nx][ny] == -105:
                break
            
            x, y = nx, ny
        
        return ret
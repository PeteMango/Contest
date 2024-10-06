from typing import List
class Solution:
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # e, s, w, n
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0]) # size of the matrix
        move_idx = 0 # tracks the direction it is moving in
        ret = [] # stores the final answer
        x, y = 0, 0 # stores current index in the 2d matrix

        while True:
            ret.append(matrix[x][y])
            matrix[x][y] = -105 # some out of bound number to show its been visited
            nx, ny = x + self.dir[move_idx][0], y + self.dir[move_idx][1]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or matrix[nx][ny] == -105:
                move_idx = (move_idx + 1) % 4
            else:
                x, y = nx, ny
                continue

            nx, ny = x + self.dir[move_idx][0], y + self.dir[move_idx][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or matrix[nx][ny] == -105:
                break

            x, y = nx, ny
        return ret

s = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]

assert s.spiralOrder(matrix) == [1,2,3,6,9,8,7,4,5], s.spiralOrder(matrix)

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

assert s.spiralOrder(matrix) == [1,2,3,4,8,12,11,10,9,5,6,7], s.spiralOrder(matrix)

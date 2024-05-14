from typing import List

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        friends = []

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    friends.append((i, j))

        def cost(x, y: int):
            sum = 0
            for i, j in friends:
                sum += abs(x-i) + abs(y-j)
            return sum

        finalx, finaly = 0, 0

        l, r, mid = 0, n-1, 0
        while l <= r:
            mid = (l + r) // 2
            if mid == n-1 or mid == 0:
                break

            if cost(mid, 0) < cost(mid+1, 0) and cost(mid, 0) < cost(mid-1, 0):
                break

            if cost(mid, 0) > cost(mid+1, 0):
                l = mid + 1
            else:
                r = mid - 1

        finalx = mid

        if finalx < n-1:
            finalx = finalx if cost(finalx, 0) < cost(finalx+1, 0) else finalx+1
        if finalx > 0:
            finalx = finalx if cost(finalx, 0) < cost(finalx-1, 0) else finalx-1

        l, r, mid = 0, m-1, 0
        while l <= r:
            mid = l + (r-l) // 2
            if mid == m-1 or mid == 0:
                break

            if cost(0, mid) < cost(0, mid+1) and cost(0, mid) < cost(0, mid-1):
                break

            if cost(0, mid) > cost(0, mid+1):
                l = mid + 1
            else:
                r = mid - 1

        finaly = mid

        if finaly < m-1:
            finaly = finaly if cost(0, finaly) < cost(0, finaly+1) else finaly+1
        if finaly > 0:
            finaly = finaly if cost(0, finaly) < cost(0, finaly-1) else finaly-1

        return cost(finalx, finaly)

s = Solution()

grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]

grid = [[1,1]]

print(s.minTotalDistance(grid))

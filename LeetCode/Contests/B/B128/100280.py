from typing import List

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        if len(points) == 1:
            return 1

        x_val = []
        for point in points:
            x_val.append(point[0])


        x_val.sort()

        n = len(x_val)

        ans, cur, i = 0, x_val[0], 0

        while i < n:
            cur = x_val[i]
            while i < n and (x_val[i] - cur) <= w:
                i += 1

            ans += 1

        return ans

s = Solution()

points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]]
w = 1

points = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]
w = 2

points = [[2,3],[1,2]]
w = 0

print(s.minRectanglesToCoverPoints(points, w))

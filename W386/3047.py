from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        ret, n = 0, len(bottomLeft)

        for i in range(n):
            for j in range(i+1, n):
                min_x = max(bottomLeft[i][0], bottomLeft[j][0])
                max_x = min(topRight[i][0], topRight[j][0])

                min_y = max(bottomLeft[i][1], bottomLeft[j][1])
                max_y = min(topRight[i][1], topRight[j][1])

                if min_x < max_x and min_y < max_y:
                    side_len = min(max_x - min_x, max_y - min_y)

                    ret = max(ret, side_len * side_len)

        return ret

s = Solution()

# bottomLeft = [[1,1],[2,2],[3,1]]
# topRight = [[3,3],[4,4],[6,6]]

# bottomLeft = [[1,1],[2,2],[1,2]]
# topRight = [[3,3],[4,4],[3,4]]

bottomLeft = [[1,1],[3,3],[3,1]]
topRight = [[2,2],[4,4],[4,2]]

print(s.largestSquareArea(bottomLeft, topRight))

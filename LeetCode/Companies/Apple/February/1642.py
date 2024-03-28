from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)

        heap = []
        for i in range(1, n):
            jump = heights[i] - heights[i-1]

            if jump > 0:
                heapq.heappush(heap, jump)

            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)

                if bricks < 0:
                    return i-1

        return n-1

s = Solution()

heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1

heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2

heights = [14,3,19,3]
bricks = 17
ladders = 0

print(s.furthestBuilding(heights, bricks, ladders))

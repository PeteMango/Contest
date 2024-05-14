# Sat, May 11, 2024

import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratio = sorted([(w / q, q) for w, q in zip(wage, quality)])
        max_heap = []
        quality_sum = 0
        max_ratio = 0.0

        for i in range(k):
            max_ratio = max(max_ratio, ratio[i][0])
            quality_sum += ratio[i][1]
            heapq.heappush(max_heap, -ratio[i][1])

        res = max_ratio * quality_sum

        for i in range(k, len(quality)):
            max_ratio = max(max_ratio, ratio[i][0])
            quality_sum += ratio[i][1] + heapq.heappop(max_heap)
            heapq.heappush(max_heap, -ratio[i][1])
            res = min(res, max_ratio * quality_sum)

        return res

s = Solution()

quality = [10,20,5]
wage = [70,50,30]
k = 2

quality = [3,1,10,10,1]
wage = [4,8,2,2,7]
k = 3

print(s.mincostToHireWorkers(quality, wage, k))

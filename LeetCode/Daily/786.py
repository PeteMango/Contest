# Fri, May 10, 2024

from heapq import heappush, heappop
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i in range(len(arr) - 1):
            heappush(heap, (arr[i]/arr[-1], i, len(arr) - 1))

        for i in range(k-1):
            res, l, r = heappop(heap)
            heappush(heap, (arr[l]/arr[r-1], l, r - 1))

        ans, l, r = heappop(heap)

        return [arr[l], arr[r]]

s = Solution()

arr = [1,2,3,5]
k = 3

arr = [1,7]
k = 1

s = print(s.kthSmallestPrimeFraction(arr, k))

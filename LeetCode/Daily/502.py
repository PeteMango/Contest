# Sat, June 15, 2024

from typing import List
from heapq import heappush, heappop
from sortedcontainers import SortedList, SortedDict

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        k = 2
        w = 0
        profits = [1, 2, 3]
        capital = [0, 1, 1]

        projects = [(0, 1), (1, 3), (1, 2)]
        k = 2
        w = 0
        pick (0, 1)

        projects = [(1, 3), (1, 2)]
        k = 1
        w = 1
        pick(1, 2)

        k = 0
        w = 0
        """

        projects = sorted(zip(capital, profits))

        mxheap = []
        idx = 0

        for i in range(k):
            while idx < len(profits) and projects[idx][0] <= w:
                heappush(mxheap, -projects[idx][1])
                idx += 1

            if len(mxheap) == 0:
                break

            w += -heappop(mxheap)

        return w

s = Solution()

k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]

k = 3
w = 0
profits = [1,2,3]
capital = [0,1,2]

print(s.findMaximizedCapital(k, w, profits, capital))

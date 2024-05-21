# 2

from typing import List

class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        ans = appleCost.copy()
        upd = True

        while upd:
            upd = False

            for a, b, cost in roads:
                a, b = a-1, b-1

                newa, newb = ans[b] + (k+1) * cost, ans[a] + (k+1)*cost

                if newa < ans[a]:
                    ans[a] = newa
                    upd = True

                if newb < ans[b]:
                    ans[b] = newb
                    upd = True
        return ans

s = Solution()

n = 4
roads = [[1,2,4],[2,3,2],[2,4,5],[3,4,1],[1,3,4]]
appleCost = [56,42,102,301]
k = 2

n = 3
roads = [[1,2,5],[2,3,1],[3,1,2]]
appleCost = [2,3,1]
k = 3

print(s.minCost(n, roads, appleCost, k))

from sortedcontainers import SortedList
from typing import List
from collections import defaultdict

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        sl = SortedList()
        d = defaultdict(int)
        sl.add(0)
        results = []

        for query in queries:
            if query[0] == 1:
                sl.add(query[1])
                idx = sl.index(query[1])

                for i in range(idx, len(sl)):
                    d[sl[i]] = max(d[sl[i-1]], sl[i] - sl[i - 1])

            else:
                _, x, sz = query
                idx = sl.bisect_right(x) - 1

                if sl[idx] <= x and (x - sl[idx] >= sz):
                    results.append(True)
                else:
                    results.append(d[sl[idx]] >= sz)

        return results

s = Solution()

queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]

queries = [[2, 1, 1]]

queries = [[1,3],[2,4,2]]

queries = [[1,1],[1,11],[1,4],[1,8],[2,13,7]]

queries = [[1,5],[1,7],[2,4,11],[2,7,3]]

print(s.getResults(queries))

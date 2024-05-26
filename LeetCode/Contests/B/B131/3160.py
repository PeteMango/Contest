from typing import List
from collections import defaultdict

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        l = defaultdict(int)
        ret = [0] * len(queries)

        for i, q in enumerate(queries):
            x, y = q[0], q[1]
            if x not in l:
                d[y].append(x)
                l[x] = y
                ret[i] = len(d)
                continue

            cur = l[x]
            # has color
            if len(d[cur]) == 1:
                del d[cur]
                l[x] = y
                d[y].append(x)
                ret[i] = len(d)

            # more than one color
            else:
                d[cur].remove(x)
                l[x] = y
                d[y].append(x)
                ret[i] = len(d)

        return ret

s = Solution()

limit = 4
queries = [[1,4],[2,5],[1,3],[3,4]]

limit = 4
queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]

print(s.queryResults(limit, queries))

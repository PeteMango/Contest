# Sat, April 20, 2024

from collections import deque, defaultdict
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        vis = [False] * n
        vis[source] = True

        d = defaultdict(list)
        for start, dest in edges:
            d[start].append(dest)
            d[dest].append(start)

        q = deque()
        q.append(source)

        while q:
            front = q[-1]
            q.pop()
            vis[front] = True

            for e in d[front]:
                if not vis[e]:
                    q.append(e)

        return vis[destination]

s = Solution()

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5

print(s.validPath(n, edges, source, destination))

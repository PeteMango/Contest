import heapq
from typing import List

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        G = [[] for _ in range(n)]
        for u, v, time in edges:
            G[u].append((v, time))
            G[v].append((u, time))

        def dijkstra() -> List[int]:
            q = [(0, 0)]
            dist = [int(1e9 + 5)] * n
            dist[0] = 0
            visited = set()

            while q:
                time, node = heapq.heappop(q)
                if node in visited:
                    continue
                visited.add(node)

                if time > disappear[node]:
                    continue

                for neighbor, t in G[node]:
                    d = time + t
                    if d < dist[neighbor] and d < disappear[neighbor]:
                        dist[neighbor] = d
                        heapq.heappush(q, (d, neighbor))

            for i in range(n):
                if dist[i] == int(1e9 + 5) or dist[i] > disappear[i]:
                    dist[i] = -1

            return dist

        return dijkstra()


s = Solution()

n = 3
edges = [[0, 1, 2], [1, 2, 1], [0, 2, 4]]
disappear = [1, 1, 5]

n = 3
edges = [[0,1,2],[1,2,1],[0,2,4]]
disappear = [1,3,5]

n = 2
edges = [[0,1,1]]
disappear = [1,1]

print(s.minimumTime(n, edges, disappear))

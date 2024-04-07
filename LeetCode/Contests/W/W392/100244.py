from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        G = defaultdict(list)
        for u, v, w in edges:
            G[u].append((v, w))
            G[v].append((u, w))

        min_cost = dict()

        def bfs(start: int):
            q = deque([start])
            visited = {start: 131071}

            while q:
                current_node = q.popleft()
                current_cost = visited[current_node]

                for neighbor, cost in G[current_node]:
                    new_cost = current_cost & cost
                    if neighbor not in visited or new_cost < visited[neighbor]:
                        visited[neighbor] = new_cost
                        q.append(neighbor)

            for node in visited:
                min_cost[(start, node)] = visited[node]
                if start != node:
                    min_cost[(node, start)] = visited[node]

        for node in range(n):
            bfs(node)

        results = []
        for s, t in queries:
            if s == t:
                results.append(0)
            else:
                results.append(min_cost.get((s, t), -1))
        return results

s = Solution()

n = 5
edges = [[0,1,7],[1,3,7],[1,2,1]]
query = [[0,3],[3,4]]

# n = 3
# edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]]
# query = [[1,2]]

# n = 9
# edges = [[0, 4, 7], [3, 5, 1], [1, 3, 5], [1, 5, 1]]
# query = [[0, 4], [1, 5], [3, 0], [3, 3], [3, 2], [2, 0], [7, 7], [7, 0]]

print(s.minimumCost(n, edges, query))

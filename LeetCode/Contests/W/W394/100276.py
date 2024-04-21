from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for i, (u, v, w) in enumerate(edges):
            graph[u].append((v, w, i))
            graph[v].append((u, w, i))

        min_heap = [(0, 0)]
        distances = [float('inf')] * n
        distances[0] = 0
        predecessors = {i: [] for i in range(n)}

        while min_heap:
            dist, node = heappop(min_heap)
            if dist > distances[node]:
                continue
            for neighbor, weight, edge_idx in graph[node]:
                distance = dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = [(node, edge_idx)]
                    heappush(min_heap, (distance, neighbor))
                elif distance == distances[neighbor]:
                    predecessors[neighbor].append((node, edge_idx))

        visited = [False] * len(edges)
        def dfs(node):
            if node == 0:
                return
            for pred, edge_idx in predecessors[node]:
                if not visited[edge_idx]:
                    visited[edge_idx] = True
                    dfs(pred)

        dfs(n - 1)
        return visited

s = Solution()

n = 6
edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]

n = 4
edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]]

print(s.findAnswer(n, edges))

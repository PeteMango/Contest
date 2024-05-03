# Sun, April 28, 2024

from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = [0] * n
        count = [1] * n

        def postorder(node, parent=None):
            for child in graph[node]:
                if child == parent:
                    continue
                postorder(child, node)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]
            
        def preorder(node, parent=None):
            for child in graph[node]:
                if child == parent:
                    continue
                ans[child] = ans[node] - count[child] + (n - count[child])
                preorder(child, node)
        
        postorder(0)
        preorder(0)

        print(count)
        print(ans)
        
        return ans

s = Solution()

n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]

n = 1
edges = []

n = 2
edges = [[1,0]]

print(s.sumOfDistancesInTree(n, edges))

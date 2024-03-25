from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        teams = [0] * 105

        for result in edges:
            teams[result[1]] = 1

        num_undefeated = 0

        for i in range(n):
            if teams[i] == 0:
                num_undefeated += 1

        if num_undefeated > 1:
            return -1

        for i in range(n):
            if teams[i] == 0:
                return i

s = Solution()

# n = 4
# edges = [[0,2],[1,3],[1,2]]

n = 3
edges = [[0,1],[1,2]]

print(s.findChampion(n=n, edges=edges))

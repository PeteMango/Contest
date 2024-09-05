# Thu, August 29, 2024

from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(x, y):
            if (x, y) in vis:
                return
            vis.add((x, y))
            for nx, ny in stones:
                if nx == x or ny == y:
                    dfs(nx, ny)
        
        vis = set()
        num_islands = 0
        
        for x, y in stones:
            if (x, y) not in vis:
                dfs(x, y)
                num_islands += 1
        
        return len(stones) - num_islands
    

s = Solution()

stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]

stones = [[0,0]]

print(s.removeStones(stones))
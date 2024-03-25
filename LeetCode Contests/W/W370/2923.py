from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for team_num, team in enumerate(grid):
            is_champion = True
            for index, result in enumerate(team):
                if index != team_num and result == 0:
                    is_champion = False
                    break

            if is_champion:
                return team_num

        return -1

s = Solution()

grid = [[0,1],[0,0]]
grid = [[0,0,1],[1,0,1],[0,0,0]]

print(s.findChampion(grid))

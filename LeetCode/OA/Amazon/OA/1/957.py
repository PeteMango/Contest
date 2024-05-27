from typing import List

class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        def update(c: list[int]) -> list[int]:
            n = len(c)
            new = [0] * n

            for i in range(1, n - 1):
                if c[i - 1] == c[i + 1]:
                    new[i] = 1
                else:
                    new[i] = 0

            return new

        vis = {}
        is_fast_forwarded = False

        while n > 0:
            if not is_fast_forwarded:
                state_tuple = tuple(cells)
                if state_tuple in vis:
                    n %= vis[state_tuple] - n
                    is_fast_forwarded = True
                else:
                    vis[state_tuple] = n

            if n > 0:
                n -= 1
                cells = update(cells)

        return cells

s = Solution()

cells = [0,1,0,1,1,0,0,1]
n = 7

cells = [1,0,0,1,0,0,1,0]
n = 1000000000

print(s.prisonAfterNDays(cells, n))

# Sat, May 25, 2024

from functools import lru_cache


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 3

        @lru_cache(100)
        def dfs(idx, num_abs, cons_late: int) -> int:
            if idx == n:
                return 1

            total_ways = dfs(idx+1, num_abs, 0)
            if num_abs < 1:
                total_ways += dfs(idx+1, num_abs+1, 0)

            if cons_late < 2:
                total_ways += dfs(idx+1, num_abs, cons_late+1)

            return total_ways % MOD

        return dfs(0, 0, 0) % MOD


s = Solution()

n = 2

n = 1

n = 10101

print(s.checkRecord(n))

from functools import lru_cache

class Solution:
    def waysToReachStair(self, k: int) -> int:
        self.ways = 0
        if k == 0:
            return 2

        @lru_cache(None)
        def dfs(current_stair: int, current_jump: int, last_move_down: bool) -> int:
            if current_stair >= k + 2:
                return 0
            total_ways = 0
            if current_stair == k:
                total_ways += 1
            if current_stair >= 1 and not last_move_down:
                total_ways += dfs(current_stair - 1, current_jump, True)
            new_stair = current_stair + 2 ** current_jump
            if new_stair < k + 2:
                total_ways += dfs(new_stair, current_jump + 1, False)
            return total_ways

        return dfs(1, 0, False)

s = Solution()

k = 0

k = 1

k = 2

k = 1048556

k = 1048559

print(s.waysToReachStair(k))

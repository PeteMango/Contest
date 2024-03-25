from typing import List

class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        # nums = [1,1,0,0,0,1,1,0,0,1]
        #
        if k == 1:
            return 0 if 1 in nums else 2

        return 0

s = Solution()

nums = [1,1,0,0,0,1,1,0,0,1]
k = 3
maxChanges = 1

print(s.minimumMoves(nums, k, maxChanges))

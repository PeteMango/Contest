# Sun, May 26, 2024

from typing import List
from bisect import bisect_left


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(1, len(nums)+1):
            if len(nums) - bisect_left(nums, i) == i:
                return i

        return -1


s = Solution()

nums = [3, 5]

nums = [0, 0]

nums = [0, 4, 3, 0, 4]

print(s.specialArray(nums))

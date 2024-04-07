# Sun, March 24, 2024

from typing import List
from statistics import mode


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return mode(nums)

s = Solution()

nums = [1,3,4,2,2]

nums = [3,1,3,4,2]

nums = [3,3,3,3,3]

print(s.findDuplicate(nums))

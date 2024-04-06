# Sun, March 24, 2024

from typing import List
from statistics import mode


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return mode(nums)

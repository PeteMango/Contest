# Mon, March 25, 2024

from typing import List
from collections import defaultdict

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        for key, val in d.items():
            if val > 1:
                ret.append(key)

        return ret

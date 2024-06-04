# Fri, May 31, 2024

from typing import List
from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        ret = []
        for key, val in d.items():
            if val == 1:
                ret.append(key)

        return ret

s = Solution()

nums = [1,2,1,3,2,5]

nums = [-1,0]

nums = [0,1]

print(s.singleNumber(nums))

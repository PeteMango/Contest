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

s = Solution()

nums = [4,3,2,7,8,2,3,1]

nums = [1,1,2]

nums = [1]

print(s.findDuplicates(nums))

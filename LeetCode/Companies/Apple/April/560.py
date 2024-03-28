from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ret = 0
        psa = 0
        d = defaultdict(int)

        d[0] = 1
        for num in nums:
            psa = psa + num

            if psa - k in d:
                ret += d[psa - k]

            d[psa] += 1

        return ret

s = Solution()

nums = [1,1,1]
k = 2

nums = [1,2,3]
k = 3

nums = [0, 0]
k = 0

print(s.subarraySum(nums, k))

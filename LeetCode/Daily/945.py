# Fri, June 14, 2024

from typing import List
from collections import defaultdict

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ans = 0
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        keys = sorted(d)
        for i in range(len(keys) - 1):
            k, nextk = keys[i], keys[i+1]
            freq = d[k] # 2
            extra = freq - 1 # 1
            vals = nextk - k - 1 # 1
            if vals == 0:
                d[nextk] += extra
                ans += extra
            else:
                if vals >= extra:
                    ans += (1 + extra) * extra // 2
                else:
                    # if not enough space, have to carry over
                    ans += (extra + extra - vals + 1) * vals // 2
                    ans += extra - vals
                    d[nextk] += (extra - vals)

        if d[keys[-1]] > 1:
            extra = d[keys[-1]] - 1
            ans += (1 + extra) * extra // 2

        return ans

s = Solution()

nums = [1,2,2]

nums = [3,2,1,2,1,7]

print(s.minIncrementForUnique(nums))

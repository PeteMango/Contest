# Sat, March 30, 2024

from typing import List
from collections import defaultdict

class Solution:
    def atMostKDistinct(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        l = 0
        ans = 0
        for r in range(len(nums)):
            if d[nums[r]] == 0:
                k -= 1
            d[nums[r]] += 1

            while k < 0:
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    k += 1
                l += 1

            ans += (r - l + 1)
        return ans

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostKDistinct(nums, k) - self.atMostKDistinct(nums, k - 1)

s = Solution()

nums = [1,2,1,2,3]
k = 2

# nums = [1,2,1,3,4]
# k = 3

print(s.subarraysWithKDistinct(nums, k))

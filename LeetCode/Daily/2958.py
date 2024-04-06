# Thu, March 28, 2024

from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        l, r, mx = 0, 0, 1

        while l <= r and r < len(nums):
            d[nums[r]] += 1
            while d[nums[r]] > k:
                d[nums[l]] -= 1
                l += 1
            mx = max(mx, r-l+1)
            r += 1

        return mx

s = Solution()

nums = [1,2,3,1,2,3,1,2]
k = 2

nums = [1,2,1,2,1,2,1,2]
k = 1

nums = [5,5,5,5,5,5,5]
k = 4

print(s.maxSubarrayLength(nums, k))

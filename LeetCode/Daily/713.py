# Wed, March 27, 2024

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product, ans = 1, 0
        l, r = 0, 0

        while l <= r and r < len(nums):
            product *= nums[r]

            while product >= k and l <= r:
                product //= nums[l]
                l += 1

            ans += (r - l + 1)
            r += 1

        return ans

s = Solution()

nums = [10,5,2,6]
k = 100

nums = [1,2,3]
k = 0

print(s.numSubarrayProductLessThanK(nums, k))

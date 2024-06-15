# Sat, June 8, 2024

from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}
        cumulative_sum = 0

        for i, num in enumerate(nums):
            cumulative_sum += num
            remainder = cumulative_sum % k if k != 0 else cumulative_sum

            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i

        return False

s = Solution()

nums = [23,2,4,6,7]
k = 6

nums = [23,2,6,4,7]
k = 6

nums = [23,2,6,4,7]
k = 13

print(s.checkSubarraySum(nums, k))

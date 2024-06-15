# Sun, June 9, 2024

from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        remainder_count = {0: 1}

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder < 0:
                remainder += k

            if remainder in remainder_count:
                count += remainder_count[remainder]
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1

        return count

s = Solution()

nums = [4,5,0,-2,-3,1]
k = 5

nums = [5]
k = 9

print(s.subarraysDivByK(nums, k))

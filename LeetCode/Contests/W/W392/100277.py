from typing import List
from statistics import median

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        if median(nums) == k:
            return 0

        nums.sort()
        ret = 0

        for i in range(len(nums)):
            if i < len(nums) // 2:
                ret += max(0, nums[i] - k)
            elif i == len(nums) // 2:
                ret += abs(k - nums[i])
            else:
                ret += max(0, k - nums[i])

        return ret

s = Solution()

nums = [2,5,6,8,5]
k = 4

nums = [2,5,6,8,5]
k = 7

nums = [1,2,3,4,5,6]
k = 4

print(s.minOperationsToMakeMedianK(nums, k))

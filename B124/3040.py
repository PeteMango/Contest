from typing import List
from functools import cache


def maxOperations(nums: List[int]) -> int:
    if len(nums) <= 2:
        return 1

    N = len(nums)

    @cache
    def dp(i=0, j=N-1, sum=0):
        if j <= i:
            return 0

        front, back, both = 0, 0, 0

        if not sum or nums[i]+nums[i+1] == sum:
            front = 1 + dp(i+2, j, nums[i]+nums[i+1])

        if not sum or nums[j]+nums[j-1] == sum:
            back = 1 + dp(i, j-2, nums[j]+nums[j-1])

        if not sum or nums[i]+nums[j] == sum:
            both = 1 + dp(i+1, j-1, nums[i]+nums[j])

        return max(front, back, both)

    return dp()


# nums = [3, 2, 1, 2, 3, 4]
nums = [3, 2, 6, 1, 4]
print(maxOperations(nums))

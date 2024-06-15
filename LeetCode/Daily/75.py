# Wed, June 12, 2024

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, 0
        for num in nums:
            if num == 0:
                zero += 1
            if num == 1:
                one += 1
            if num == 2:
                two += 1

        for i in range(zero):
            nums[i] = 0

        for i in range(zero, zero + one):
            nums[i] = 1

        for i in range(zero + one, zero + one + two):
            nums[i] = 2

s = Solution()

nums = [2,0,2,1,1,0]

nums = [2,0,1]

print(s.sortColors(nums))

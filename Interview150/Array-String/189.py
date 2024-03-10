from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        i, j = len(nums) - k, 0,
        t = i
        ret = []
        while i < len(nums):
            ret.append(nums[i])
            i += 1

        while j < t:
            ret.append(nums[j])
            j += 1

        for i, _ in enumerate(nums):
            nums[i] = ret[i]


s = Solution()

# nums = [1,2,3,4,5,6,7]
# k = 3

# nums = [-1,-100,3,99]
# k = 2

nums = [1, 2]
k = 5

s.rotate(nums, k)
print(nums)

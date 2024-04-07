from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        mx, cur = -1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
            else:
                mx = max(mx, cur)
                cur = 1

        mx = max(mx, cur)

        cur = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                cur += 1
            else:
                mx = max(mx, cur)
                cur = 1

        mx = max(mx, cur)

        return mx

s = Solution()

nums = [1,4,3,3,2]

nums = [3,3,3,3]

nums = [3,2,1]

print(s.longestMonotonicSubarray(nums))

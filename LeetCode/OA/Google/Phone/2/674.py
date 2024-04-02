from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        mx_len, cur = -1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
                continue
            else:
                mx_len = max(mx_len, cur)
                cur = 1

        return max(mx_len, cur)

s = Solution()

nums = [1,3,5,4,7]

nums = [2,2,2,2,2]

nums = [2, 1]

print(s.findLengthOfLCIS(nums))

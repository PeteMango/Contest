# Sun, March 31, 2024

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans, mx_occur, mn_occur = 0, -1, -1

        l, r = 0, 0
        while r < len(nums):
            if nums[r] < minK or nums[r] > maxK:
                l = r + 1
                r += 1
                continue

            if nums[r] == minK:
                mn_occur = r

            if nums[r] == maxK:
                mx_occur = r

            ans += 0 if min(mx_occur, mn_occur) - l + 1 < 0 else min(mx_occur, mn_occur) - l + 1
            r += 1

        return ans

s = Solution()

nums = [1,3,5,2,7,5]
minK = 1
maxK = 5

nums = [1,1,1,1]
minK = 1
maxK = 1

print(s.countSubarrays(nums, minK, maxK))

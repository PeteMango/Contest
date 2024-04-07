# Tue, March 26, 2024

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        found = [0] * int(1e5 + 5)

        for x in nums:
            if x >= 0 and x < 1e5 + 5:
                found[x] += 1

        for i in range(1, len(found)):
            if found[i] == 0:
                return i

        return -1

s = Solution()

nums = [1,2,0]

nums = [3,4,-1,1]

nums = [7,8,9,11,12]

print(s.firstMissingPositive(nums))

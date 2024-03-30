from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        shortest = len(nums) + 1

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if self.subArrayOr(nums, i, j) >= k:
                    # print(f'shortest: {shortest}')
                    shortest = min(shortest, j-i+1)

        return -1 if shortest == len(nums) + 1 else shortest

    def subArrayOr(self, nums: List[int], i, j: int) -> int:
        ans = 0

        for x in range(i, j+1):
            ans |= nums[x]

        return ans

s = Solution()

nums = [1,2,3]
k = 2

nums = [2,1,8]
k = 10

nums = [1,2]
k = 0

print(s.minimumSubarrayLength(nums, k))

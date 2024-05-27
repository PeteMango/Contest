# Sun, May 19, 2024

from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ret = 0
        for i in range(2**(len(nums))):
            ret += self.xor(nums, i)

        return ret

    def xor(self, nums: List[int], mask: str):
        ans = 0
        for i in range(len(nums)):
            if (mask >> i) & 1:
                ans ^= nums[i]

        return ans


s = Solution()

nums = [1, 3]

nums = [5, 1, 6]

nums = [3, 4, 5, 6, 7, 8]

print(s.subsetXORSum(nums))

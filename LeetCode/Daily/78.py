# Mon, May 20, 2024

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        for i in range(2**(len(nums))):
            ret.append(self.subset(nums, i))

        return ret

    def subset(self, nums: List[int], mask: int):
        ans = []
        for i in range(len(nums)):
            if (mask >> i) & 1:
                ans.append(nums[i])

        return ans


s = Solution()

nums = [1, 2, 3]

nums = [0]

print(s.subset(nums))

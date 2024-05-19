from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i-1] % 2:
                return False
        return True

s = Solution()

nums = [1]

nums = [2,1,4]

nums = [4,3,1,6]

print(s.isArraySpecial(nums))

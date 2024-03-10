from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for val in nums:
            if gas < 0:
                return False
            if val > gas:
                gas = val
            gas -= 1

        return True

s = Solution()

# nums = [2,3,1,1,4]

nums = [3,2,1,0,4]

print(s.canJump(nums))

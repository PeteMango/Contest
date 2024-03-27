from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = 5005
        for x in nums:
            if x < min:
                min = x

        return min

s = Solution()

nums = [3,4,5,1,2]

# nums = [4,5,6,7,0,1,2]

nums = [11,13,15,17]

print(s.findMin(nums))

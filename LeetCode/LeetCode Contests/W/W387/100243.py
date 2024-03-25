from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return nums

        a,b = [], []

        a.append(nums[0])
        b.append(nums[1])

        for i in range(2, len(nums)):
            if a[-1] > b[-1]:
                a.append(nums[i])
            else:
                b.append(nums[i])

        return a + b

s = Solution()

# nums = [2,1,3]

nums = [5,4,3,8]

print(s.resultArray(nums))

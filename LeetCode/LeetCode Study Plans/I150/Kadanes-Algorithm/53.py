from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        curSum, mxSum = 0, int(-1e9 + 5)

        for num in nums:
            curSum += num

            if curSum > mxSum:
                mxSum = curSum

            if curSum < 0:
                curSum = 0

        return mxSum


s = Solution()

# nums = [-2,1,-3,4,-1,2,1,-5,4]

# nums = [1]

nums = [5,4,-1,7,8]

print(s.maxSubArray(nums))

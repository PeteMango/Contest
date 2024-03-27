from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n, mxSum = len(nums), self.maxSubArray(nums)

        for i in range(n):
            nums = nums[-1:] + nums[:-1]

            mxSum = max(mxSum, self.maxSubArray(nums))

        return mxSum


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

# nums = [1,-2,3,-2]

# nums = [5,-3,5]

nums = [-3,-2,-3]

print(s.maxSubarraySumCircular(nums))

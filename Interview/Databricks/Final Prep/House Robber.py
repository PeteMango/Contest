from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        dp = [nums[0]] + [max(nums[0], nums[1])] + (n-2) * [0]
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        print(dp)
        return max(dp)

s = Solution()

nums = [1,2,3,1]
assert s.rob(nums) == 4

nums = [2,7,9,3,1]
assert s.rob(nums) == 12

nums = [2,1,1,2]
assert s.rob(nums) == 4

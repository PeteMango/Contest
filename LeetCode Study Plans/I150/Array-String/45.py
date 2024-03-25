from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [10005] * len(nums)
        dp[0] = 0

        for i, val in enumerate(nums):
            for j in range(i, min(len(nums), i + val + 1)):
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[-1]

s = Solution()

# nums = [2,3,1,1,4]

nums = [2,3,0,1,4]

print(s.jump(nums))

from typing import List

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        toAdd = []
        dp = [0] * len(nums)
        for x in nums:
            toAdd.append(k - x if k - x >= 0 else 0)

        for i in range(len(nums)):
            dp[i] = toAdd[i]

            if i-3 >= 0:
                dp[i] += dp[i-3]

            if i-1 >= 0:
                dp[i] = min(dp[i], toAdd[i] + dp[i-1])

            if i-2 >= 0:
                dp[i] = min(dp[i], toAdd[i] + dp[i-2])

        print(dp)
        return min(dp[len(nums) - 1], dp[len(nums) - 2], dp[len(nums) - 3])

s = Solution()

nums = [2,3,0,0,2]
k = 4

print(s.minIncrementOperations(nums, k))

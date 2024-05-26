from typing import List

class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        dp = [0] * n

        if len(nums) == 1:
            ans = 0
            for x, y in queries:
                nums[x] = y
                ans += max(0, nums[0]) % MOD
            return ans % MOD

        def build(nums):
            dp[0] = max(0, nums[0])
            dp[1] = max(dp[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        def update(idx, nums):
            if idx == 0:
                dp[0] = max(0, nums[0])
                if n > 1:
                    dp[1] = max(dp[0], nums[1])
            elif idx == 1:
                dp[1] = max(dp[0], nums[1])
            for i in range(max(2, idx), n):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        build(nums)

        ans = 0
        for x, y in queries:
            nums[x] = y
            if x < 2:
                build(nums)
            else:
                update(x, nums)
            ans += dp[-1] % MOD

        return ans % MOD

s = Solution()

nums = [3,5,9]
queries = [[1,-2],[0,-3]]

nums = [0,-1]
queries = [[0,-5]]

print(s.maximumSumSubsequence(nums, queries))

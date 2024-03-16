from typing import List

class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def dp(i, k, c):
            if i == n:
                return 2**(n-c) if k==0 else 0

            ans = dp(i+1, k, c)
            if k >= nums[i]:
                ans += dp(i+1, k-nums[i], c+1)
            return ans%int(1e9 + 7)
        return dp(0, k, 0)

s = Solution()
nums = [1, 1, 3, 2, 4, 2, 2, 1, 4, 1, 2, 4, 4, 3, 3, 4, 1, 3, 3, 3, 2, 1, 4, 1, 2]
k = 5

nums = [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]
k = 49

print(s.sumOfPower(nums, k))

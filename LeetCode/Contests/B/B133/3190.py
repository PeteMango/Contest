from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            ans += min(num % 3, 1)

        return ans


s = Solution()

nums = [1, 2, 3, 4]

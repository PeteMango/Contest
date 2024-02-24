from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        psa = [0] * n

        for i, num in enumerate(nums):
            if i >= 1:
                psa[i] = psa[i-1] + nums[i]
            else:
                psa[i] = nums[i]

        if psa[n-1] < target:
            return 0

        l, r, mn = 0, 0, int(1e5 + 5)

        while l <= r and r < n:
            sum = self.psaSum(psa, l, r)

            if sum >= target:
                mn = min(mn, r - l + 1)
                l += 1
            elif sum < target:
                r += 1

        return mn

    def psaSum(self, psa: List[int], l, r: int) -> int:
        if l == 0:
            return psa[r]

        return psa[r] - psa[l-1]

s = Solution()

# target = 7
# nums = [2,3,1,2,4,3]

# target = 4
# nums = [1,4,4]

# target = 11
# nums = [1,1,1,1,1,1,1,1]

target = 6
nums = [10,2,3]

print(s.minSubArrayLen(target, nums))

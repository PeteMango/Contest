from typing import List
from itertools import combinations
from math import comb

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7

        def power_of_subsequence(sub):
            return min(abs(a - b) for a, b in combinations(sub, 2))

        subsequences = list(combinations(nums, k))
        sum_of_powers = sum(power_of_subsequence(sub) for sub in subsequences) % MOD

        return sum_of_powers


s = Solution()

nums = [1,2,3,4]
k = 3

nums = [2,2]
k = 2

nums = [4,3,-1]
k = 2

print(s.sumOfPowers(nums, k))

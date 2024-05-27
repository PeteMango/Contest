# Wed, May 22, 2024

from typing import List
from collections import defaultdict


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.output = 0

        def dfs(start, seen):
            if start >= len(nums):
                return
            for i in range(start, len(nums)):
                if len(seen) != 0 and seen[nums[i]-k] != 0 or seen[nums[i]+k] != 0:
                    continue
                seen[nums[i]] += 1
                self.output += 1
                dfs(i+1, seen)
                seen[nums[i]] -= 1
            return
        dfs(0, defaultdict(int))
        return self.output


s = Solution()

nums = [2, 4, 6]
k = 2

nums = [1]
k = 1

print(s.beautifulSubsets(nums))

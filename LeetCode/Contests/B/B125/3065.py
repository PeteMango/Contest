from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0

        for num in nums:
            if num < k:
                cnt += 1

        return cnt

s = Solution()

# nums = [2,11,10,1,3]
# k = 10

# nums = [1,1,2,4,9]
# k = 1

nums = [1,1,2,4,9]
k = 9

print(s.minOperations(nums, k))

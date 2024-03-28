from typing import List
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        of = defaultdict(int)
        mx_sum = 0

        cur_sum = 0

        for i in range(k):
            d[nums[i]] += 1

            if d[nums[i]] >= 2:
                of[nums[i]] = d[nums[i]]

            cur_sum += nums[i]

        print(of)
        if len(of) == 0:
            mx_sum = cur_sum

        i = k
        while i < len(nums):
            if nums[i-k] in of:
                if of[nums[i-k]] == 2:
                    of.pop(nums[i-k])
                else:
                    of[nums[i-k]] -= 1

            d[nums[i - k]] -= 1
            d[nums[i]] += 1

            if d[nums[i]] >= 2:
                of[nums[i]] = d[nums[i]]

            print(of)
            cur_sum += nums[i] - nums[i-k]

            if len(of) <= 0:
                mx_sum = max(mx_sum, cur_sum)

            i += 1

        return mx_sum

s = Solution()

nums = [1,5,4,2,9,9,9]
k = 3

# nums = [4,4,4]
# k = 3

# nums = [9,9,9,1,2,3]
# k = 3

print(s.maximumSubarraySum(nums, k))

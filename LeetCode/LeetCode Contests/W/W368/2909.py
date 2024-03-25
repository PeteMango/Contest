from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        prefix_min, suffix_min = [0] * len(nums), [0] * len(nums)
        prefix_min[0] = nums[0]
        suffix_min[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix_min[i] = min(prefix_min[i-1], nums[i])

        for i in range(len(nums)-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i])
        
        min_sum = int(1e9 + 5)
        for i in range(1, len(nums)-1, 1):
            if prefix_min[i-1] >= nums[i] or suffix_min[i+1] >= nums[i]:
                continue
            min_sum = min(min_sum, prefix_min[i-1] + nums[i] + suffix_min[i+1])

        return -1 if min_sum == int(1e9 + 5) else min_sum

s = Solution()

nums = [8,6,1,5,3]

nums = [5,4,8,7,10,2]

print(s.minimumSum(nums))

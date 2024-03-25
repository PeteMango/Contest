from typing import List
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        min_sum, n = int(1e5 + 5), len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[j] > nums[i] and nums[j] > nums[k]:
                        min_sum = min(min_sum, nums[i]+nums[j]+nums[k])
        return -1 if min_sum == int(1e5 + 5) else min_sum

s = Solution()

nums = [8,6,1,5,3]

nums = [5,4,8,7,10,2]

nums = [6,5,4,3,4,5]

print(s.minimumSum(nums))

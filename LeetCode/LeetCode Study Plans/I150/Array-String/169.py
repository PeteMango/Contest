from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority, majority_occurance = nums[0], 0

        for i, val in enumerate(nums):
            if i < 1:
                continue

            if val == majority:
                majority_occurance += 1
            else:
                majority_occurance -= 1
                if majority_occurance < 0:
                    majority_occurance = 0
                    majority = val

        return majority

s = Solution()

# nums = [3,2,3]

nums = [2,2,1,1,1,2,2]

print(s.majorityElement(nums))

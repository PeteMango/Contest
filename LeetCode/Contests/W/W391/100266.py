from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        count = 0
        current_sequence_length = 1

        for i in range(1, len(nums)):

            if nums[i] != nums[i - 1]:
                current_sequence_length += 1
            else:
                count += (current_sequence_length * (current_sequence_length + 1)) // 2
                current_sequence_length = 1

        count += (current_sequence_length * (current_sequence_length + 1)) // 2

        return count

s = Solution()

nums = [0,1,1,1]

nums = [1,0,1,0]

nums = [1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1]

print(s.countAlternatingSubarrays(nums))

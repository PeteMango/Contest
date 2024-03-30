from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_len = len(nums) + 1
        current_or = 0
        bit_frequency = [0] * 32

        left = 0
        right = 0

        def update_frequency(val, delta):
            for i in range(32):
                if val & (1 << i):
                    bit_frequency[i] += delta

        while right < len(nums):
            update_frequency(nums[right], 1)
            current_or = sum((1 << i) for i in range(32) if bit_frequency[i] > 0)

            while current_or >= k and left <= right:
                min_len = min(min_len, right - left + 1)
                update_frequency(nums[left], -1)
                current_or = sum((1 << i) for i in range(32) if bit_frequency[i] > 0)
                left += 1

            right += 1

        return min_len if min_len != len(nums) + 1 else -1

s = Solution()

nums = [1,2,3]
k = 2

nums = [2,1,8]
k = 10

# nums = [1,2]
# k = 0

# nums = [1,2,32,21]
# k = 55

print(s.minimumSubarrayLength(nums, k))

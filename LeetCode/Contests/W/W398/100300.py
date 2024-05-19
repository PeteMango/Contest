from typing import List

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        num_digits = len(str(nums[0]))

        digit_counts = [[0] * 10 for _ in range(num_digits)]

        for num in nums:
            num_str = str(num)
            for i, digit in enumerate(num_str):
                digit_counts[i][int(digit)] += 1

        total_diff = 0

        for i in range(num_digits):
            for d in range(10):
                count_d = digit_counts[i][d]
                if count_d > 0:
                    total_diff += count_d * (n - count_d)

        return total_diff // 2

s = Solution()

nums = [13,23,12]

nums = [10,10,10,10]

print(s.sumDigitDifferences(nums))

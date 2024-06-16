from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        remainder_count = {}
        count = 0

        for hour in hours:
            remainder = hour % 24
            complement = (24 - remainder) % 24

            if complement in remainder_count:
                count += remainder_count[complement]


            if remainder in remainder_count:
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1

        return count

s = Solution()

hours = [12,12,30,24,24]

hours = [72,48,24,3]

print(s.countCompleteDayPairs(hours))

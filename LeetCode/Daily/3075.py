# Thu, May 9, 2024

from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        num_picked, i, sum = 0, 0, 0

        while num_picked < k:
            sum += max(0,happiness[i] - num_picked)

            num_picked += 1
            i += 1

        return sum

s = Solution()

happiness = [1,2,3]
k = 2

happiness = [1,1,1,1]
k = 2

happiness = [2,3,4,5]
k = 1

print(s.maximumHappinessSum(happiness, k))

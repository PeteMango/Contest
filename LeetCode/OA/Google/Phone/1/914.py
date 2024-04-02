import math
from typing import List
from collections import defaultdict

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = defaultdict(int)

        for num in deck:
            d[num] += 1

        divisors = self.getDivisors(len(deck))
        divisors.sort()

        for num in divisors:
            if num == 1:
                continue
            if self.canPartition(d, num):
                return True

        return False

    def canPartition(self, d: defaultdict, num: int) -> bool:
        for key, val in d.items():
            if val % num != 0:
                return False
        return True

    def getDivisors(self, n: int) -> List[int]:
        ret = []
        for i in range(1, n, 1):
            if n % i == 0:
                ret.append(i)
                ret.append(n // i)
        return list(set(ret))

s = Solution()

deck = [1,2,3,4,4,3,2,1]

deck = [1,1,1,2,2,2,3,3]

deck = [1,1,1,1,2,2,2,2,2,2]

deck = [1]

print(s.hasGroupsSizeX(deck))

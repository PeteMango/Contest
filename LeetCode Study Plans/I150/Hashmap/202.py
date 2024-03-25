from typing import List
from collections import defaultdict

class Solution:
    def isHappy(self, n: int) -> bool:
        already = defaultdict(int)
        already[n] += 1

        while True:
           digits = self.digits(n)

           sum = self.sum(digits)
           print(f'sum is {sum}')

           if sum == 1:
               return True

           if sum in already:
               return False
           else:
               already[sum] += 1

           n = sum

        return False

    def digits(self, n: int) -> List[int]:
        ret = []
        while n > 0:
            ret.append(int(n % 10))
            n = int(n / 10)

        return ret

    def sum(self, dig: List[int]) -> int:
        sum = 0

        for d in dig:
            sum += d*d

        return sum

s = Solution()

# n = 19

n = 2

print(s.isHappy(n))

import math
from collections import defaultdict

class Solution:
    def minAnagramLength(self, s: str) -> int:
        d = defaultdict(int)
        for c in s:
            d[c] += 1

        gcd = math.gcd(*d.values())

        ans = 0
        for num in d.values():
            ans += num // gcd

        return ans

s = Solution()

str = "abba"

str = "cdef"

print(s.minAnagramLength(str))

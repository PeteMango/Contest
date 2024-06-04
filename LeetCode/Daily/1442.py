# Thu, May 30, 2024

from typing import List

class Solution:
    def countTriplets(self, a: List[int]) -> int:
        def xorsum(l, r: int) -> int:
            if l == 0:
                return pxor[r]
            return pxor[r] ^ pxor[l-1]

        pxor = [0] * len(a)
        pxor[0] = a[0]
        for i in range(1,len(a)):
            pxor[i] = pxor[i-1] ^ a[i]

        ans = 0
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                if j-i < 1:
                    continue
                # print(f'xor of {i} {j} is  {xorsum(i, j)}')
                if xorsum(i, j) == 0:
                    ans += (j-i)
        return ans

s = Solution()

arr = [2,3,1,6,7]

arr = [1,1,1,1,1]

print(s.countTriplets(arr))

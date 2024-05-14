from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        paircost = [0] * (n - 1)

        for i in range(1, n):
            paircost[i-1] = weights[i] + weights[i-1]

        paircost.sort()
        ans = 0
        for i in range(k-1):
            ans += paircost[n - 2 - i] - paircost[i]

        return ans

s = Solution()

weights = [1,3,5,1]
k = 2

weights = [1, 3]
k = 2

print(s.putMarbles(weights, k))

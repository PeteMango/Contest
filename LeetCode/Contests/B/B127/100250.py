from typing import List

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)

        psa = possible
        for i in range(1, n):
            psa[i] += psa[i-1]

        print(psa)

        min_len = n+1
        for i in range(0, n-1):
            # print(f'{self.psaSum(psa, 0, i)} {self.psaSum(psa, i, n-1)}')
            if self.psaSum(psa, 0, i) > self.psaSum(psa, i+1, n-1):
                min_len = i+1
                break

        return -1 if min_len == n+1 else min_len

    def psaSum(self, psa: List[int], i, j: int) -> int:
        len = j-i+1
        sum = 0

        if i == 0:
            sum = psa[j]
        else:
            sum = psa[j] - psa[i-1]

        return sum - (len - sum)

s = Solution()

possible = [1,0,1,0]

# possible = [1,1,1,1,1]

# possible = [0,0]

# possible = [1, 1]

print(s.minimumLevels(possible))

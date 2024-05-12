from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [0] * len(energy)
        print(energy)

        for i in range(k):
            dp[i] = energy[i]

        ans = -10**5-5
        for i in range(k, len(energy)):
            dp[i] = max(dp[i-k] + energy[i], energy[i])

        for i in range(len(energy) - k, len(energy)):
            ans = max(ans, dp[i])

        print(dp)
        return ans

s = Solution()

energy = [5,2,-10,-5,1]
k = 3

# energy = [-2,-3,-1]
# k = 2

print(s.maximumEnergy(energy, k))

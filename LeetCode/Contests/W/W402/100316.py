from typing import List
from collections import defaultdict

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        if not power:
            return 0

        freq = defaultdict(int)
        for p in power:
            freq[p] += 1

        unique_powers = sorted(freq.keys())

        dp = defaultdict(int)

        for i in range(len(unique_powers)):
            damage = unique_powers[i]
            current_damage = damage * freq[damage]

            for j in range(max(0, i - 10), i):
                if abs(damage - unique_powers[j]) > 2:
                    current_damage = max(current_damage, damage * freq[damage] + dp[unique_powers[j]])

            dp[damage] = current_damage

        return max(dp.values())

s = Solution()

power = [1,1,3,4]

power = [7,1,6,6]

print(s.maximumTotalDamage(power))

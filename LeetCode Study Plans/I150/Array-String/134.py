from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank, idx, n = 0, 0, len(gas)

        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank, idx = 0, i+1

        return idx

s = Solution()

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

gas = [2,3,4]
cost = [3,4,3]

print(s.canCompleteCircuit(gas, cost))

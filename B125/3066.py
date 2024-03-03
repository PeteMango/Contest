from typing import List
from collections import deque

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        smaller = []

        for num in nums:
            if num < k:
                smaller.append(num)

        smaller.sort()

        cnt = 0

        dq = deque(smaller)

        while len(dq) >= 2:
            print(dq)
            x, y = dq[0], dq[1]

            for i in range(2):
                dq.popleft()

            res = min(x, y) * 2 + max(x, y)

            if res < k:
                dq.append(res)

            cnt += 1

        print(f'smaller at the end {dq}')

        if len(dq) == 1:
            return cnt + 1

        return cnt


s = Solution()

nums = [2,11,10,1,3]
k = 10

nums = [1,1,2,4,9]
k = 20

nums = [61,81,12,29,3,96,96,28,38,71]
k = 97

print(s.minOperations(nums, k))

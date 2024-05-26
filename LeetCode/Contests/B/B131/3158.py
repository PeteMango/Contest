from typing import List
from collections import defaultdict

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        appear = []
        for key, val in d.items():
            if val == 2:
                appear.append(key)

        if len(appear) == 0:
            return 0

        ans = appear[0]
        for i in range(1, len(appear)):
            ans ^= appear[i]

        return ans

s = Solution()

nums = [1,2,1,3]

nums = [1,2,3]

nums = [1,2,2,1]

print(s.duplicateNumbersXOR(nums))

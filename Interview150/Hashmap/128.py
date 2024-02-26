from collections import defaultdict
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dict = defaultdict(int)

        for num in nums:
            dict[num] += 1

        ret = 1

        for key in dict:
            if key-1 in dict:
                continue

            t = key+1
            while t in dict:
                t += 1

            ret = max(ret, t-key)

        return ret

s = Solution()

# nums = [100,4,200,1,3,2]

nums = [0,3,7,2,5,8,4,6,0,1]

# nums = []

print(s.longestConsecutive(nums))

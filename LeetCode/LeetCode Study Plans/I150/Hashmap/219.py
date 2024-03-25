from collections import defaultdict
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = defaultdict(list)

        for index, num in enumerate(nums):
            dict[num].append(index)

        for key, indicies in dict.items():
            for i in range(len(indicies) - 1):
                if indicies[i + 1] - indicies[i] <= k:
                   return True

        return False

s = Solution()

# nums = [1,2,3,1]
# k = 3

# nums = [1,0,1,1]
# k = 1

nums = [1,2,3,1,2,3]
k = 2

print(s.containsNearbyDuplicate(nums, k))

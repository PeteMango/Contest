from sortedcontainers import SortedList
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        sl = SortedList()
        for i in range(k):
            sl.add(nums[i])

        ans.append(sl[-1])
        for i in range(k, n):
            sl.remove(nums[i-k])
            sl.add(nums[i])
            ans.append(sl[-1])

        return ans

s = Solution()

nums = [1,3,-1,-3,5,3,6,7]
k = 3

nums = [1]
k = 1

print(s.maxSlidingWindow(nums, k))

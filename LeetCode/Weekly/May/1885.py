# 1

from typing import List
from bisect import bisect_right

class Solution:
    def countPairs(self, a: List[int], b: List[int]) -> int:
        # a[i] + a[j] > b[i] + b[j]
        # a[i] - b[i] > b[j] - a[j]

        d = sorted(x - y for x, y in zip(a, b))
        ans, n = 0, len(d)

        for i, x in enumerate(d):
            idx = bisect_right(d, -x, i+1)
            ans += n - idx

        return ans

s = Solution()

nums1 = [2,1,2,1]
nums2 = [1,2,1,2]

nums1 = [1,10,6,2]
nums2 = [1,4,1,5]

print(s.countPairs(nums1, nums2))

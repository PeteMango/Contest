from sortedcontainers import SortedList
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sl = SortedList()

        for num in nums1:
            sl.add(num)
        for num in nums2:
            sl.add(num)

        if len(sl) % 2 == 0:
            l, r = sl[len(sl) // 2 - 1], sl[len(sl) // 2]

            return float((l + r) / 2)
        else:
            return sl[len(sl) // 2]

s = Solution()

nums1 = [1,3]
nums2 = [2]

nums1 = [1,2]
nums2 = [3,4]

print(s.findMedianSortedArrays(nums1, nums2))

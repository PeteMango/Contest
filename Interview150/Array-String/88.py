from typing import List

class Solution:
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(n):
            a[i+m] = b[i]

        a.sort()

        return

s = Solution()

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5

s.merge(nums1, m, nums2, n)
print(nums1)

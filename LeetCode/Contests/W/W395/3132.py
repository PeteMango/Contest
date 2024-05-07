from typing import List

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        n = len(nums1)

        def findx(i, j: int) -> int:
            t = nums1.copy()
            del t[j]
            del t[i]

            for i in range(1, n-2):
                if t[i] - nums2[i] != t[i-1] - nums2[i-1]:
                    return 10**9+5

            return nums2[0] - t[0]

        min_ans = 10**9+5
        for i in range(n):
            for j in range(i+1, n):
                min_ans = min(min_ans, findx(i, j))

        return min_ans

s = Solution()

nums1 = [4,20,16,12,8]
nums2 = [14,18,10]

nums1 = [3,5,5,3]
nums2 = [7,7]

print(s.minimumAddedInteger(nums1, nums2))

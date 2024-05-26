from sortedcontainers import SortedList
from typing import List
from collections import defaultdict

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def factors(n):
            return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

        d = defaultdict(int)
        for i in range(len(nums2)):
            d[nums2[i]*k] += 1

        ans = 0
        for num in nums1:
            fact = factors(num)
            for f in fact:
                if f in d:
                    ans += d[f]
        return ans

s = Solution()

nums1 = [1,3,4]
nums2 = [1,3,4]
k = 1

nums1 = [1,2,4,12]
nums2 = [2,4]
k = 3

pritn(s.numberOfPairs(nums1, nums2, k))

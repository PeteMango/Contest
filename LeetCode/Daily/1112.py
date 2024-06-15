# Tue, June 11, 2024

from typing import List
from collections import defaultdict

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = defaultdict(int)
        s = set()
        for num in arr2:
            s.add(num)

        for num in arr1:
            d[num] += 1

        ret = []
        end = []
        for num in arr2:
            if num in d:
                for j in range(d[num]):
                    ret.append(num)

        for key, val in d.items():
            if key not in s:
                for i in range(val):
                    end.append(key)

        end.sort()
        ans = ret + end
        return ans

s = Solution()

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]

print(s.relativeSortArray(arr1, arr2))

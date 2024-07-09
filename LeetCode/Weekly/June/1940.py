from typing import List
from collections import defaultdict

class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        d = defaultdict(int)
        ret = []

        for arr in arrays:
            for num in arr:
                d[num] += 1

        for key, val in d.items():
            if val == len(arrays):
                ret.append(key)

        return sorted(ret)

s = Solution()

arrays = [[1,3,4], [1,4,7,9]]

arrays = [[2,3,6,8], [1,2,3,5,6,7,10], [2,3,4,6,9]]

arrays = [[1,2,3,4,5], [6,7,8]]

print(s.longestCommonSubsequence(arrays))

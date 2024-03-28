from typing import List
from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = set()
        d = defaultdict(int)

        for val in arr:
            d[val] += 1

        for key, val in d.items():
            s.add(val)

        return len(s) == len(d)

s = Solution()

arr = [1,2,2,1,1,3]

arr = [1,2]

arr = [-3,0,1,-3,1,1,1,-3,10,0]

print(s.uniqueOccurrences(arr))

from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        d = defaultdict(int)
        sl = SortedList()
        ret = []

        for key, val in zip(nums, freq):
            # print(sl)
            if key in d:
                sl.remove(d[key])
                d[key] += val
                sl.add(d[key])
            else:
                d[key] = val
                sl.add(d[key])
            ret.append(sl[-1])
        return ret


s = Solution()

nums = [2,3,2,1]
freq = [3,2,-3,1]

nums = [5,5,3]
freq = [2,-2,1]

print(s.mostFrequentIDs(nums, freq))

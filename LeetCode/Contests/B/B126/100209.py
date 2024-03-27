from typing import List
from collections import deque

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum = 0
        mp = {}
        for idx, num in enumerate(nums):
            sum += num

            if num not in mp:
                d = deque()
                d.append(idx)
                mp[num] = d
            else:
                mp[num].append(idx)


        print(mp)
        ret = []
        for q in queries:
            idx, topop = q[0], q[1]
            num = nums[idx]

            if not mp:
                ret.append(0)
                continue

            if num in mp and idx in mp[num]:
                mp[num].remove(idx)
                sum -= num

            while topop > 0 and mp:
                for key in sorted(list(mp.keys())):
                    val = mp[key]
                    if len(val) <= topop:
                        sum -= len(val) * key
                        topop -= len(val)
                        mp.pop(key)
                    else:
                        for x in range(topop):
                            sum -= key
                            mp[key].popleft()
                        topop = 0

                    if not mp:
                        break

            ret.append(sum)
        return ret


s = Solution()

nums = [1,2,2,1,2,3,1]
queries = [[1,2],[3,3],[4,2]]

# nums = [1,4,2,3]
# queries = [[0,1]]

print(s.unmarkedSumArray(nums, queries))

from typing import List
from sortedcontainers import SortedList

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a = SortedList()
        b = SortedList()

        ret_a, ret_b = [], []

        a.add(nums[0])
        b.add(nums[1])

        ret_a.append(nums[0])
        ret_b.append(nums[1])

        for i in range(2, len(nums)):
            num_a = len(a) - a.bisect_right(nums[i])
            num_b = len(b) - b.bisect_right(nums[i])

            if num_a == num_b:
                if len(a) <= len(b):
                    ret_a.append(nums[i])
                    a.add(nums[i])
                else:
                    ret_b.append(nums[i])
                    b.add(nums[i])
            elif num_a > num_b:
                ret_a.append(nums[i])
                a.add(nums[i])
            else:
                ret_b.append(nums[i])
                b.add(nums[i])

        return ret_a + ret_b

s = Solution()

nums = [2,1,3,3]

nums = [5,14,3,1,2]

nums = [3,3,3,3]

print(s.resultArray(nums))

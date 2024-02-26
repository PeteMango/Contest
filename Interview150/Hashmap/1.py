from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = defaultdict(int)
        for num in nums:
            dict[num] += 1

        print(dict)

        search_for = []
        for num in nums:
            dict[num] -= 1

            if dict[target - num] == 1:
                search_for = [num, target - num]

        ret = []
        for index, num in enumerate(nums):
            if num == search_for[0]:
                ret.append(index)
            elif num == search_for[1]:
                ret.append(index)

        return ret



s = Solution()

nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6

# nums = [3,3]
# target = 6

print(s.twoSum(nums, target))

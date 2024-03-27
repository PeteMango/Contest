from typing import List
from collections import defaultdict

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        dict = defaultdict(int)

        for num in nums:
            dict[num] += 1

        size = int(len(nums) / 2)

        cnt = 0

        for key in dict:
            if dict[key] > 2:
                return False

        s = set()

        for key in dict:
            if dict[key] == 2:
                dict[key] -= 1
                s.add(key)

            if len(s) == size:
                break

        for key in dict:
            if dict[key] == 1 and key not in s:
                dict[key] -= 1
                s.add(key)

            if len(s) == size:
                break

        print(s)

        if len(s) < size:
            return False

        print(dict)

        for key in dict:
            if dict[key] > 1:
                return False

        return True

s = Solution()

# nums = [1,1,2,2,3,4]

# nums = [1,1,1,1]

nums = [2,10,2,7,8,9,7,6,6,9]

print(s.isPossibleToSplit(nums))

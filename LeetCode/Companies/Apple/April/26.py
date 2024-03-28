from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt, i = 0, 0

        numsSet = set(nums)

        for x in numsSet:
            nums[i] = x
            i += 1

        for i in range(len(numsSet), len(nums)):
            nums[i] = 101

        nums.sort()
        return len(numsSet)

s = Solution()

nums = [1,1,2]

nums = [0,0,1,1,1,2,2,3,3,4]

print(s.removeDuplicates(nums))

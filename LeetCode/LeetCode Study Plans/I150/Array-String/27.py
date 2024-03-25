from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 51
            else:
                cnt += 1

        nums.sort()

        return cnt

s = Solution()

nums = [0,1,2,2,3,0,4,2]
val = 2

print(s.removeElement(nums, val))
print(nums)

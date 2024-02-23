from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt, n = 0, len(nums)
        for i in range(n):
            cnt, t = 2, i

            while i < n:
                if nums[i] == nums[t]:
                    if cnt <= 0:
                        nums[i] = int(1e4 + 5)
                    else:
                        cnt -= 1
                else:
                    break
                i += 1

        nums.sort()

        ret = 0
        for x in nums:
            if x != int(1e4 + 5):
                ret += 1

        return ret

s = Solution()

# nums = [1,1,1,2,2,3]

nums = [0,0,1,1,1,1,2,3,3]

print(s.removeDuplicates(nums))
print(nums)

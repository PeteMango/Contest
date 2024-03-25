from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()

        nums.sort()

        for i in range(len(nums) - 2):
            j, k = i+1, len(nums) - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ret.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1

        return list(ret)


s = Solution()

nums = [-1,0,1,2,-1,-4]

# nums = [0,1,1]

# nums = [0,0,0]

print(s.threeSum(nums))

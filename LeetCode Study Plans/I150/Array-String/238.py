from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zero, total_product = 0, 1
        for val in nums:
            if val == 0:
                num_zero += 1
            else:
                total_product *= val

        if num_zero > 1:
            return [0] * len(nums)

        if num_zero == 1:
            ret = []
            for val in nums:
                if val == 0:
                    ret.append(total_product)
                else:
                    ret.append(0)
            return ret

        if num_zero == 0:
            ret = []
            for val in nums:
                ret.append(int(total_product / val))
            return ret

s = Solution()

# nums = [1,2,3,4]

nums = [-1,1,0,-3,3]

print(s.productExceptSelf(nums))

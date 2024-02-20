from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        maxXOR = 0
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums), 1):
                if self.isStrong(nums[i], nums[j]):
                    maxXOR = max(maxXOR, nums[i]^nums[j])

        return maxXOR

    def isStrong(self, a, b: int) -> bool:
        return abs(a - b) <= min(a, b)

s = Solution()

# nums = [1,2,3,4,5]
# nums = [10,100]
nums = [5,6,25,30]

print(s.maximumStrongPairXor(nums))

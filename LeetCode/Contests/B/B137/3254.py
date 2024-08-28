from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        def isSorted(i, j: int, nums: List[int]) -> bool:
            for x in range(i+1, j+1):
                if nums[x] != nums[x-1] + 1:
                    return False
            return True
        
        ans = []
        for i in range(len(nums) - k + 1):
            if isSorted(i, i + k - 1, nums):
                ans.append(nums[i + k - 1])
            else:
                ans.append(-1)
        
        return ans
    
s = Solution()

nums = [1,2,3,4,3,2,5]
k = 3

nums = [2,2,2,2,2]
k = 4

nums = [3,2,3,2,3,2]
k = 2

print(s.resultsArray(nums, k))
# Thu, May 2, 2024

from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        pos = []
        d = defaultdict(int)

        for num in nums:
            d[num] = 1
            if num > 0:
                pos.append(num)
            
        pos.sort(reverse=True)
        for positive in pos:
            if -positive in d:
                return positive
            
        return -1
        
s = Solution()

nums = [-1,2,-3,3]

nums = [-1,10,6,7,-7,1]

nums = [-10,8,6,7,-2,-3]

print(s.findMaxK(nums))
from typing import List
import math

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        nums.sort()

        ret, mxArray= 0, max(nums)

        if mxArray == 0:
            return 0

        numBinary = int(math.log2(int(mxArray))) + 1

        for i in range(0, numBinary, 1):
            tmpCnt = 0
            for x in nums:
                if (x & (1<<i)) > 0:
                    tmpCnt += 1

            # print(f'{tmpCnt} {i}')
            if tmpCnt >= k:
                ret += (1<<i)

        return ret

s = Solution()

# nums = [7,12,9,8,9,15]
# k = 4

# nums = [2,12,1,11,4,5]
# k = 6

nums = [10,8,5,9,11,6,8]
k = 1

print(s.findKOr(nums, k))

from typing import List
from typing_extensions import DefaultDict

def maxSelectedElements(nums: List[int]) -> int:
    dp = DefaultDict(int)
    nums.sort()

    for x in nums:
        dp[x+1] = dp[x] + 1
        dp[x] = dp[x-1] + 1

    return max(dp.values())

# nums = [2,1,5,1,1]
nums = [1,4,7,10]

print(maxSelectedElements(nums))

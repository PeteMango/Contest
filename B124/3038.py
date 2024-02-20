from typing import List


def maxOperations(nums: List[int]) -> int:
    if len(nums) <= 2:
        return 1

    cnt, sum = 1, nums[0]+nums[1]
    for i in range(2, len(nums) - 1, 2):
        if nums[i]+nums[i+1] == sum:
            cnt += 1
        else:
            return cnt

    return cnt


# nums = [3, 2, 6, 1, 4]
nums = [1, 1, 1, 1, 1, 1]

print(maxOperations(nums))

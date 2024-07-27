#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinimumOperations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY executionTime
#  2. INTEGER x
#  3. INTEGER y
#

import heapq


def getMinimumOperations(executionTime, x, y):
    hp = []

    for time in executionTime:
        hp.append(-time)

    ans = 0

    heapq.heapify(hp)
    while hp:
        mx = -hp[0]
        nums = []
        while hp:
            nums.append(heapq.heappop(hp))

        num_major = mx // x
        if num_major == 0:
            num_major = 1
        ans += num_major
        nums[0] += x * num_major
        for i in range(1, len(nums)):
            nums[i] += y * num_major

        for num in nums:
            if num < 0:
                heapq.heappush(hp, num)

    return ans

    # while executionTime:


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    executionTime_count = int(input().strip())

    executionTime = []

    for _ in range(executionTime_count):
        executionTime_item = int(input().strip())
        executionTime.append(executionTime_item)

    x = int(input().strip())

    y = int(input().strip())

    result = getMinimumOperations(executionTime, x, y)

    fptr.write(str(result) + "\n")

    fptr.close()

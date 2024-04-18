#!/bin/python3

from typing import List
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr: List[int]) -> None:
    # Write your code here

    asum, minval, maxval = 0, 10 ** 9 + 7, -1

    for num in arr:
        asum += num
        minval = min(minval, num)
        maxval = max(maxval, num)

    print(f'{asum - maxval} {asum - minval}')


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

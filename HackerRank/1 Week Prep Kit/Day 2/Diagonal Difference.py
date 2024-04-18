#!/bin/python3

from typing import List
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr: List[List[int]]) -> int:
    n, l, r = len(arr), 0, 0
    for i in range(n):
        l += arr[i][i]

    for i in range(n):
        r += arr[i][n-1-i]

    return abs(r-l)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def sumDigits(n: str) -> int:
    ans = 0
    for c in n:
        ans += int(c)
    return ans

def superDigit(n: str, k: int) -> int:
    super_dig = sumDigits(n) * k
    return helper(str(super_dig))

def helper(n: str) -> int:
    if len(n) == 1:
        return int(n)
    return helper(str(sumDigits(n)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

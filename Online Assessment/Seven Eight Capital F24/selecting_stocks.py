#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'selectStock' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER saving
#  2. INTEGER_ARRAY currentValue
#  3. INTEGER_ARRAY futureValue
#

def selectStock(saving, currentValue, futureValue):
    dp = [0] * (saving+1)
    n = len(currentValue)

    for i in range(n):
        for j in range(saving, currentValue[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - currentValue[i]] + futureValue[i] - currentValue[i])

    return dp[saving]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    saving = int(input().strip())

    currentValue_count = int(input().strip())

    currentValue = []

    for _ in range(currentValue_count):
        currentValue_item = int(input().strip())
        currentValue.append(currentValue_item)

    futureValue_count = int(input().strip())

    futureValue = []

    for _ in range(futureValue_count):
        futureValue_item = int(input().strip())
        futureValue.append(futureValue_item)

    result = selectStock(saving, currentValue, futureValue)

    fptr.write(str(result) + '\n')

    fptr.close()

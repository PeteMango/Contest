#!/bin/python3
from typing import List
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr: List[int]) -> None:
    pos, neg, zero = 0, 0, 0
    for num in arr:
        if num == 0:
            zero += 1
        elif num > 0:
            pos += 1
        else:
            neg += 1

    n = len(arr)

    print(pos / n)
    print(neg / n)
    print(zero / n)

    return

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

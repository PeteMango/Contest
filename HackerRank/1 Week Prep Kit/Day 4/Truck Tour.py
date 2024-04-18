#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

from typing import List
def truckTour(petrolpumps: List[List[int]]) -> int:
    curGas, startIdx = 0, 0
    for idx, station in enumerate(petrolpumps):
        curGas += station[0] - station[1]

        if curGas < 0:
            curGas = 0
            startIdx = idx + 1

    return startIdx


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()

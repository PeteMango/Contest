#!/bin/python3

from typing import List
import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps: int, path: str) -> int:
    inValley, curHeight, numValley = False, 0, 0
    for direction in path:
        if direction == 'U':
            curHeight += 1
        else:
            curHeight -= 1

        if curHeight == 0 and inValley:
            numValley += 1
            inValley = False
        elif curHeight < 0:
            inValley = True
        else:
            inValley = False

    return numValley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

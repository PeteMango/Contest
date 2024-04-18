#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s: str) -> int:
    ans = 0
    for idx, c in enumerate(s):
        if (idx + 1) % 3 == 1:
            ans += 1 if c != 'S' else 0

        if (idx + 1) % 3 == 2:
            ans += 1 if c != 'O' else 0

        if (idx + 1) % 3 == 0:
            ans += 1 if c != 'S' else 0

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

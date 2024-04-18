#!/bin/python3

from collections import defaultdict
import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s: str) -> str:
    d = defaultdict(int)
    for c in s:
        if c == ' ':
            continue
        d[c.lower()] += 1

    return 'pangram' if len(d) == 26 else 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

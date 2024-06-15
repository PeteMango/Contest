#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'deleteProducts' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ids
#  2. INTEGER m
#

from collections import defaultdict

def deleteProducts(ids, m):
    d = defaultdict(int)
    for num in ids:
        d[num] += 1

    unique = len(d)
    freq = []
    for key, val in d.items():
        freq.append(val)

    freq.sort()
    for i in range(len(freq)):
        if m >= freq[i]:
            unique -= 1
            m -= freq[i]
    return unique


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ids_count = int(input().strip())

    ids = []

    for _ in range(ids_count):
        ids_item = int(input().strip())
        ids.append(ids_item)

    m = int(input().strip())

    result = deleteProducts(ids, m)

    fptr.write(str(result) + '\n')

    fptr.close()

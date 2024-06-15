#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reassignedPriorities' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY priorities as parameter.
#
import bisect

def reassignedPriorities(priorities):
    sl = []
    s = set()

    for num in priorities:
        if num in s:
            continue
        else:
            s.add(num)
            sl.append(num)

    sl.sort()
    ret = []
    for p in priorities:
        idx = bisect.bisect_left(sl, p)
        if idx != len(sl) and sl[idx] == p:
            ret.append(idx+1)
    return ret



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    priorities_count = int(input().strip())

    priorities = []

    for _ in range(priorities_count):
        priorities_item = int(input().strip())
        priorities.append(priorities_item)

    result = reassignedPriorities(priorities)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

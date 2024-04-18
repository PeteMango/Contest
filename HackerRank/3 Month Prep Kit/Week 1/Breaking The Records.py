#!/bin/python3

from typing import List
import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores: List[int]) -> List[int]:
    min_score, max_score, break_min, break_max = scores[0], scores[0], 0, 0
    for i in range(1, len(scores)):
        if scores[i] < min_score:
            min_score = scores[i]
            break_min += 1

        if scores[i] > max_score:
            max_score = scores[i]
            break_max += 1

    return [break_max, break_min]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

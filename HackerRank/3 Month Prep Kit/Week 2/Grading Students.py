#!/bin/python3

from typing import List
import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades: List[int]) -> List[int]:
    rounded = [0] * len(grades)

    for idx, num in enumerate(grades):
        if num < 38:
            rounded[idx] = num
        elif num >= 38 and num <= 40:
            rounded[idx] = 40
        else:
            next_multiple = ((num // 5) + 1) * 5
            if next_multiple - num < 3:
                rounded[idx] = next_multiple
            else:
                rounded[idx] = num

    return rounded

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

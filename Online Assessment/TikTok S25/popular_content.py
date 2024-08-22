#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'GetOptimalContentStorage' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY tiktokStorage as parameter.
#


def GetOptimalContentStorage(tiktokStorage):
    # find the longest continuous substr of 1s and subtract from the total
    num_ones = 0
    for num in tiktokStorage:
        if num == 1:
            num_ones += 1

    start_ones = 0
    for i in range(num_ones):
        if tiktokStorage[i] == 1:
            start_ones += 1

    end_ones = 0
    for i in range(len(tiktokStorage) - num_ones, len(tiktokStorage)):
        if tiktokStorage[i] == 1:
            end_ones += 1

    return num_ones - max(start_ones, end_ones)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    tiktokStorage_count = int(input().strip())

    tiktokStorage = []

    for _ in range(tiktokStorage_count):
        tiktokStorage_item = int(input().strip())
        tiktokStorage.append(tiktokStorage_item)

    result = GetOptimalContentStorage(tiktokStorage)

    fptr.write(str(result) + "\n")

    fptr.close()

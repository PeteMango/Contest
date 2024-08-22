#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxSharedCategories' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY favoriteCategories as parameter.
#


def maxSharedCategories(favoriteCategories):
    favoriteCategories.sort(reverse=True)
    div = [0] * 10005

    for i in range(len(div) - 1, 0, -1):
        for j in range(len(favoriteCategories)):
            if i > favoriteCategories[j]:
                break

            if favoriteCategories[j] % i == 0:
                div[i] += 1

        if div[i] >= 2:
            return i

    return 1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    favoriteCategories_count = int(input().strip())

    favoriteCategories = []

    for _ in range(favoriteCategories_count):
        favoriteCategories_item = int(input().strip())
        favoriteCategories.append(favoriteCategories_item)

    result = maxSharedCategories(favoriteCategories)

    fptr.write(str(result) + "\n")

    fptr.close()

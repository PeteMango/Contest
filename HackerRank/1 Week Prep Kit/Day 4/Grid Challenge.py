#!/bin/python3

from typing import List
import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid: List[List[str]]) -> str:
    def compare(a, b: str) -> bool:
        return ord(a) < ord(b)

    n, m = len(grid), len(grid[0])

    for i in range(n):
        grid[i] = ''.join(sorted(grid[i]))



    for i in range(m):
        for j in range(1, n):
            if compare(grid[j][i], grid[j-1][i]):
                return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s: str, k: int) -> str:
    def update(c: str) -> str:
        if not c.isalpha():
            return c

        if c.isupper():
            return str(chr((ord(c) - ord('A') + k) % 26 + ord('A')))

        return str(chr((ord(c) - ord('a') + k) % 26 + ord('a')))

    ans = ''
    for c in s:
        ans += update(c)

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s: str) -> int:
    def isPalidrome(substr: str) -> bool:
        for i in range(0, int(len(substr)/2)):
            if substr[i] != substr[len(substr)-i-1]:
                return False
        return True

    if isPalidrome(s) or len(s) == 1:
        return -1

    l, r = 0, len(s) - 1
    while l <= r:
        if s[l] == s[r]:
            l += 1
            r -= 1

        elif isPalidrome(s[l+1:r+1]):
            return l
        elif isPalidrome(s[l:r]):
            return r

    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

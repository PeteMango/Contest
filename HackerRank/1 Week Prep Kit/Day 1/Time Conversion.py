#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s: str) -> str:
    pm = True if s[-2] == 'P' else False

    if pm:
        if s[0:2] == '12':
            return s[0:-2]
        return str(int(s[0:2]) + 12) + s[2:-2]
    elif not pm and s[0:2] == '12':
        return str(int(s[0:2]) - 12) + '0' + s[2:-2]



    return s[0:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

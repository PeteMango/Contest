#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimalOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY words as parameter.
#


def helper(words: str):
    c = words[0]
    need, cur = 0, 1
    print(words)
    for i in range(1, len(words)):
        if words[i] == c:
            cur += 1
        else:
            if cur > 1:
                need += cur // 2

            cur = 1
            c = words[i]
    if cur > 1:
        need += cur // 2
    return need


def minimalOperations(words):
    # Write your code here
    ret = []
    for word in words:
        ret.append(helper(word))
    return ret


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    result = minimalOperations(words)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()

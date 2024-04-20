#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

from typing import List
from collections import deque, defaultdict

def bfs(n, m: int, edges: List[List[int]], s: int):
    d = defaultdict(list)
    for edge in edges:
        d[edge[0]].append(edge[1])
        d[edge[1]].append(edge[0])

    print(d)

    dq = deque()
    dq.append(s)

    dist = [int(1e5 + 5)] * (n+1)
    dist[s] = 0

    while dq:
        front = dq.pop()

        for nb in d[front]:
            if dist[front] + 6 < dist[nb]:
                dq.append(nb)

            dist[nb] = min(dist[nb], dist[front] + 6)

    ans = []
    for i, val in enumerate(dist):
        if i == 0 or i == s:
            continue
        if val == int(1e5 + 5):
            ans.append(-1)

        else:
            ans.append(val)

    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

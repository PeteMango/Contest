#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMaximumThroughput' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY throughput
#  2. INTEGER_ARRAY scaling_cost
#  3. INTEGER budget
#


def getMaximumThroughput(throughput, scaling_cost, budget):
    def can_achieve(min_ans: int) -> bool:
        total_cost = 0
        for i in range(len(throughput)):
            if throughput[i] < min_ans:
                need = min_ans - throughput[i]
                if need % throughput[i] == 0:
                    total_cost += (need // throughput[i]) * scaling_cost[i]
                else:
                    total_cost += ((need // throughput[i]) + 1) * scaling_cost[i]

                if total_cost > budget:
                    return False
        return total_cost <= budget

    l, r, best = 0, 10**9 + 7, min(throughput)
    while l <= r:
        mid = (l + r) // 2
        # print(mid)
        if can_achieve(mid):
            best = mid
            l = mid + 1
        else:
            r = mid - 1
    return best


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    throughput_count = int(input().strip())

    throughput = []

    for _ in range(throughput_count):
        throughput_item = int(input().strip())
        throughput.append(throughput_item)

    scaling_cost_count = int(input().strip())

    scaling_cost = []

    for _ in range(scaling_cost_count):
        scaling_cost_item = int(input().strip())
        scaling_cost.append(scaling_cost_item)

    budget = int(input().strip())

    result = getMaximumThroughput(throughput, scaling_cost, budget)

    fptr.write(str(result) + "\n")

    fptr.close()

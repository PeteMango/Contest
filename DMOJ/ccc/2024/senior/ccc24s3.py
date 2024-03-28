from typing import List

def isSubsequence(a, b: List[int]) -> bool:
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
            continue
        else:
            i += 1

    if j == len(b):
        return True

    return False

n = int(input())

a, b = [], []

numbers = list(map(int, input().split()))
a.extend(numbers)

numbers = list(map(int, input().split()))
b.extend(numbers)

bprime = [b[0]]

for i in range(1, n):
    if b[i] == bprime[-1]:
        continue
    else:
        bprime.append(b[i])

if not isSubsequence(a, bprime):
    print("NO")




print(bprime)

a = [3, 1, 2]
b = [3, 1]

print(isSubsequence(a, b))

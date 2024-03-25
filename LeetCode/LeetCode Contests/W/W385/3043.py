from typing import List


def longestCommonPrefix(arr1: List[int], arr2: List[int]) -> int:
    str_array1, str_array2 = [], []

    for i in range(len(arr1)):
        str_array1.append(str(arr1[i]))

    for i in range(len(arr2)):
        str_array2.append(str(arr2[i]))

    possible_prefix = set()

    for s in str_array1:
        t = ""
        for i in range(len(s)):
            t += s[i]
            possible_prefix.add(t)

    longest_prefix = 0

    for s in str_array2:
        t = ""
        for i in range(len(s)):
            t += s[i]
            if t in possible_prefix:
                longest_prefix = max(longest_prefix, len(t))

    return longest_prefix


# arr1 = [1, 10, 100]
# arr2 = [1000]

arr1 = [1, 2, 3]
arr2 = [4, 4, 4]

print(longestCommonPrefix(arr1, arr2))

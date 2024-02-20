from typing import List


def countPrefixSuffixPairs(words: List[str]) -> int:
    cnt = 0
    for i in range(len(words) - 1):
        for j in range(i+1, len(words), 1):
            if isTrue(words[i], words[j]):
                cnt += 1

    return cnt


def isTrue(fix, s: str) -> bool:
    return s.endswith(fix) and s.startswith(fix)


# words = ["a", "aba", "ababa", "aa"]
# words = ["pa", "papa", "ma", "mama"]
words = ["abab", "ab"]

print(countPrefixSuffixPairs(words))

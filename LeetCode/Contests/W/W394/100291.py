from collections import defaultdict
from functools import update_wrapper

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d = defaultdict(int)

        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for c in word:
            d[c] += 1

        lower_case = defaultdict(list)

        for idx, c in enumerate(word):
            if c in lower:
                lower_case[c].append(idx)

        upper_case = defaultdict(int)
        for idx, c in enumerate(word):
            if c in upper and c not in upper_case:
                upper_case[c] = idx;

        pos = []
        for i in range(26):
            if lower[i] in d and upper[i] in d:
                pos.append(lower[i])

        ans = 0
        for c in pos:
            if lower_case[c][-1] < upper_case[c.upper()]:
                ans += 1

        return ans

s = Solution()

word = "aaAbcBC"

word = "abc"

word = "AbBCab"

print(s.numberOfSpecialChars(word))

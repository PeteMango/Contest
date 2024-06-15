# Wed, June 5, 2024

from collections import defaultdict
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d = defaultdict(int)
        for c in words[0]:
            d[c] += 1

        for i in range(1, len(words)):
            t = defaultdict(int)
            for c in words[i]:
                t[c] += 1

            for key, val in d.items():
                d[key] = min(d[key], t[key])

        ret = []
        for key, val in d.items():
            for i in range(val):
                ret.append(key)
        return ret

s = Solution()

words = ["bella","label","roller"]

words = ["cool","lock","cook"]

print(s.commonChars(words))

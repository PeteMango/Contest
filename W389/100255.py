from collections import defaultdict
from typing import List

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        d = defaultdict(int)

        for char in word:
            d[char] += 1

        lst = list(d.values())
        lst.sort()

        def needToDelete(l, r) -> int:
            need = 0
            for n in lst:
                if n >= l and n <= r:
                    continue
                elif n < l:
                    need += n
                else:
                    need += n - r
            return need

        min_ans = needToDelete(lst[0], lst[0]+k)
        for i in range(lst[0], lst[-1] - k + 1):
            min_ans = min(min_ans, needToDelete(i, i+k))

        return int(min_ans)

s = Solution()

word = "aabcaba"
k = 0

word = "dabdcbdcdcd"
k = 2

word = "aaabaaa"
k = 2

word = "qdqqddxdjd"
k = 3

word = "sssn"
k = 0

word = "oppffppoffp"
k = 1

word = "k"
k = 100000

print(s.minimumDeletions(word, k))

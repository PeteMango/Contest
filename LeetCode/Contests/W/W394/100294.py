from collections import defaultdict

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d = defaultdict(int)

        for c in word:
            d[c] += 1

        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        ans = 0
        for i in range(26):
            if lower[i] in d and upper[i] in d:
                ans += 1

        return ans

s = Solution()

word = "aaAbcBC"

word = "abc"

word = "abBCab"

print(s.numberOfSpecialChars(word))

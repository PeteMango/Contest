# Tue, June 4, 2024

from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for c in s:
            d[c] += 1

        v = []
        for key, val in d.items():
            v.append(val)

        v.sort(reverse=True)
        hasOne = False
        ans = 0
        for val in v:
            if val % 2 == 0:
                ans += val
            else:
                if not hasOne:
                    ans += val
                    hasOne = True
                else:
                    ans += val - 1
        return int(ans)

s = Solution()

str = "abccccdd"

str = "a"

print(s.longestPalindrome(str))

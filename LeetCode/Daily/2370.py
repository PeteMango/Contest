# Wed, April 24, 2024

from collections import defaultdict

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        def isAdj(a, b: str) -> bool:
            if abs(ord(a) - ord(b)) <= k:
                return True
            return False

        alph = 'abcdefghijklmnopqrstuvwxyz'

        def getAdj(char: str) -> str:
            ret = ''
            for c in alph:
                if isAdj(c, char):
                    ret += c
            return ret

        dp = defaultdict(int)

        for i, c in enumerate(s):
            dp[c] += 1

            adj = getAdj(c)
            for char in adj:
                if char == c:
                    continue
                dp[c] = max(dp[c], dp[char] + 1)

        ans = 0
        for key, val in dp.items():
            ans = max(ans, val)

        return ans

s = Solution()

str = "acfgbd"
k = 2

str = "abcd"
k = 3

print(s.longestIdealString(str, k))

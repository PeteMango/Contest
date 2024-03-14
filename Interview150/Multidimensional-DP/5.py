from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, mxLen, startIdx = len(s), 0, 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            j, k = 0, i
            while k < n:
                self.solve(j, k, dp, s)

                if dp[j][k] == True:
                    mxLen = max(k-j+1, mxLen)
                    startIdx = j
                j += 1
                k += 1

        print(mxLen)
        return s[startIdx:startIdx+mxLen]

    def solve(self, i, j: int, dp: List[List[bool]], s: str):
        if i == j:
            dp[i][j] = True
            return

        if j-i == 1:
            if s[i] == s[j]:
                dp[i][j] = True
                return
            else:
                dp[i][j] = False
                return
        if s[i] == s[j] and dp[i+1][j-1] == True:
            dp[i][j] = True
            return
        else:
            dp[i][j] = False
            return

s = Solution()

str = "babad"

str = "cbbd"

str = "ccd"

print(s.longestPalindrome(str))

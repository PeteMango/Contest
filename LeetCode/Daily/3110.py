# Sat, June 1, 2024

class Solution:
    def scoreOfString(self, s: str) -> int:
        if len(s) == 1:
            return 0
        sum = 0
        for i in range(1, len(s)):
            sum += abs(ord(s[i]) - ord(s[i-1]))

        return sum

s = Solution()

str = "hello"

str = "zaz"

print(s.scoreOfString(str))

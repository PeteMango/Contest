class Solution:
    def makePalindrome(self, s: str) -> bool:
        n = len(s)
        op = 2
        for i in range(n//2):
            if s[i] != s[n - 1 - i]:
                op -= 1

        return op >= 0

s = Solution()

str = "abcdba"

str = "aa"

str = "abcdef"

print(s.makePalindrome(str))

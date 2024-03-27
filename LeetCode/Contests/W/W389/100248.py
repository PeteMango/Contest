class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if self.isInReverse(s[i:i+2], s):
                return True
        return False

    def isInReverse(self, substr, s: str) -> bool:
        reverse = s [::-1]

        return substr in reverse

s = Solution()

str = "leetcode"

str = "abcba"

str = "abcd"

str = "bcaa"

print(s.isSubstringPresent(str))

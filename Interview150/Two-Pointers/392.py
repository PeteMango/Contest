class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                i += 1
                j += 1
                continue
            else :
                j += 1

        print(f'{i} {j}')

        if i == len(s):
            return True

        return False

s = Solution()

# a = "abc"
# b = "ahbgdc"

# a = "axc"
# b = "ahbgdc"

# a = "b"
# b = "c"

# a = "aaaaaa"
# b = "bbaaaa"

a = "bb"
b = "ahbgdc"

print(s.isSubsequence(a, b))

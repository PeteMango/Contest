class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        uppercase = self.lowerToUpperCase(s)
        removed = self.removeDash(uppercase)

        ans = ""
        i = len(removed) - 1
        cur = 0
        while i >= 0:
            if cur == k:
                ans += "-"
                cur = 0

            cur += 1
            ans += removed[i]

            i -= 1

        return ans[::-1]

    def removeDash(self, s: str) -> str:
        ret = ""
        for c in s:
            if c == '-':
                continue
            ret += c
        return ret

    def lowerToUpperCase(self, s: str) -> str:
        ret = ""
        for i in range(len(s)):
            if s[i].isalpha() and s[i].islower():
                ret += s[i].upper()
            else:
                ret += s[i]
        return ret

s = Solution()

str = "5F3Z-2e-9-w"
k = 4

str = "2-5g-3-J"
k = 2

print(s.licenseKeyFormatting(str, k))

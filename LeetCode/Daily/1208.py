# Tue, May 28, 2024

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        d = [0] * len(s)
        for i in range(len(s)):
            d[i] = abs(ord(s[i]) - ord(t[i]))

        l, r, sm, ret = 0, 0, 0, 0
        while r < len(s) and l <= r:
            sm += d[r]
            r += 1

            while sm > maxCost:
                sm -= d[l]
                l += 1

            ret = max(ret, r-l)

        return ret

s = Solution()

str = "abcd"
t = "bcdf"
maxCost = 3

str = "abcd"
t = "cdef"
maxCost = 3

str = "abcd"
t = "acde"
maxCost = 0

print(s.equalSubstring(str, t, maxCost))

class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        parts = []

        for i in range(0, n, 2):
            parts.append(s[i:i+2])

        ans = 0

        for part in parts:
            if part[0] == part[1]:
                continue
            else:
                ans += 1

        return ans

s = Solution()

str = "1001"

str = "10"

str = "0000"

print(s.minChanges(str))

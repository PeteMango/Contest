class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        height = [''] * numRows

        i = 0
        while i < n:
            t = 0
            while i < n and t < numRows:
                height[t] += s[i]
                i += 1
                t += 1

            t = 0
            while i < n and t < numRows - 2:
                height[numRows - t - 2] += s[i]
                i += 1
                t += 1

        ret = ""
        for h in height:
            ret += h

        return ret

s = Solution()

# str = "PAYPALISHIRING"
# numRows = 3

# str = "PAYPALISHIRING"
# numRows = 4

str = "A"
numRows = 1

print(s.convert(str, numRows))

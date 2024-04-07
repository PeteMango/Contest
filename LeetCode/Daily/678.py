# Sat, April 6, 2024

class Solution:
    def checkValidString(self, s: str) -> bool:
        open, close = 0, 0
        for c in s:
            if c == '(':
                open += 1
            else:
                open -= 1

            if c == ')':
                close -= 1
            else:
                close += 1

            if close < 0:
                break

            open = max(open, 0)

        return open == 0

s = Solution()

str = "()"

str = "(*)"

str = "(*))"

print(s.checkValidString(str))

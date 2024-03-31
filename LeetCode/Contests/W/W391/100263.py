class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if x % self.sumofDigits(x) == 0:
            return self.sumofDigits(x)

        return -1

    def sumofDigits(self, x: int) -> int:
        ans = 0
        while x > 0:
            ans += x % 10
            x = x // 10

        return ans

s = Solution()

x = 18

x = 23

x = 1

x = 2

print(s.sumOfTheDigitsOfHarshadNumber(x))

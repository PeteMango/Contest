class Solution:
    def findNthDigit(self, n: int) -> int:
        # 1 - 9 = 9 digits
        # 10-99 = 90 * 2 = 180 digits
        # 100-999 = 900 * 3 = 1800 digits
        # 1000-9999 = 9000 * 4 = 18000 digits

        # x is constant
        # y is the scale
        # c is the num digits
        x, c, y = 9, 1, 1


        while n > (x - y + 1) * c:
            print(f'n:{n}\nx:{x}\ny:{y}\nc:{c}\n')
            n -= (x - y + 1) * c

            c += 1
            y *= 10
            x += 9 * y

        print(f'n:{n}\nx:{x}\ny:{y}\nc:{c}\n')

        dig = y + (n // c) - 1
        if n % c != 0:
            dig += 1

        pos = n % c


        print(dig)

        return self.getDig(dig, pos)

    def getDig(self, dig, pos: int) -> int:
        return int(str(dig)[pos-1])


s = Solution()

n = 3

# n = 11

n = 1000

print(s.findNthDigit(n))

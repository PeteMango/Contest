# Thu, April 11, 2024

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'

        sk = []

        for digit in num:
            while sk and k > 0 and sk[-1] > digit:
                sk.pop()
                k -= 1

            sk.append(digit)

        if k > 0:
            sk = sk[:-k]

        result = ''.join(sk).lstrip('0')

        print(f'result is {result}')

        if result:
            return result


        return '0'

s = Solution()

num = "1432219"
k = 3

num = "10200"
k = 1

num = "10"
k = 2

print(s.removeKdigits(num, k))

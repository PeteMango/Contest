class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        dig = []
        while num > 0:
            dig.append(num % 10)
            num = int(num/10)
        dig.reverse()
        for i in range(len(dig)):
            dig[i] *= pow(10, len(dig)-i-1)

        dig_char = {
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM',
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }



        for d in dig:
            print(roman)
            if d in dig_char:
                roman += dig_char[d]
            elif d < 4:
                for i in range(0, d, 1):
                    roman += "I"
            elif d < 9 and d > 5:
                roman += "V"
                for i in range(5, d, 1):
                    roman += "I"
            elif d < 40:
                for i in range(0, d, 10):
                    roman += "X"
            elif d < 90 and d > 50:
                roman += "L"
                for i in range(50, d, 10):
                    roman += "X"
            elif d < 400:
                for i in range(0, d, 100):
                    roman += "C"
            elif d < 900 and d > 500:
                 roman += "D"
                 for i in range(500, d, 100):
                     roman += "C"
            elif d > 1000:
                 for i in range(0, d, 1000):
                     roman += "M"

        return roman


s = Solution()

num = 3

num = 58

# num = 1994

print(s.intToRoman(num))

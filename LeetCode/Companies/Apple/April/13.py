class Solution:
    def romanToInt(self, s: str) -> int:
        n, ret = len(s), 0
        patterns = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        i = 0
        while i < n:
            substr = s[i:min(n, i+2)]

            if substr in patterns:
                ret += patterns[substr]
                i += 2
            else:
                ret += values[s[i]]
                i += 1

        return ret

s = Solution()

str = "III"

str = "LVIII"

str = "MCMXCIV"

print(s.romanToInt(str))

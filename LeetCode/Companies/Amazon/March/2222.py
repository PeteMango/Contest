class Solution:
    def numberOfWays(self, s: str) -> int:
        zero_left, zero_right = [0] * len(s), [0] * len(s)
        one_left, one_right = [0] * len(s), [0] * len(s)

        for i in range(1, len(s)):
            if s[i-1] == '0':
                zero_left[i] = zero_left[i-1] + 1
            else:
                zero_left[i] = zero_left[i-1]

        for i in range(len(s) - 2, -1, -1):
            if s[i+1] == '0':
                zero_right[i] = zero_right[i+1] + 1
            else:
                zero_right[i] = zero_right[i+1]

        for i in range(1, len(s)):
            if s[i-1] == '1':
                one_left[i] = one_left[i-1] + 1
            else:
                one_left[i] = one_left[i-1]

        for i in range(len(s) - 2, -1, -1):
            if s[i+1] == '1':
                one_right[i] = one_right[i+1] + 1
            else:
                one_right[i] = one_right[i+1]

        ret = 0
        for i in range(len(s)):
            if s[i] == '1' and zero_left[i] > 0 and zero_right[i] > 0:
                ret += zero_left[i] * zero_right[i]

            if s[i] == '0' and one_left[i] > 0 and one_right[i] > 0:
                ret += one_left[i] * one_right[i]

        return ret

s = Solution()

str = "001101"

str = "11100"

print(s.numberOfWays(str))

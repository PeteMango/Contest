class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sum = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    sum += abs(i-j)
        return sum

s = Solution()

str = "abc"
t = "bac"

str = "abcde"
t = "edbac"

print(s.findPermutationDifference(str, t))

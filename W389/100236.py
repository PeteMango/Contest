class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        occur = []
        for idx, char in enumerate(s):
            if char == c:
                occur.append(idx)

        num = len(occur)
        return int((1 + num)*num/2)

s = Solution()

str = "abada"
c = "a"

str = "zzz"
c = "z"

print(s.countSubstrings(str, c))

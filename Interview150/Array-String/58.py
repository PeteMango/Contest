class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n, cnt = len(s), 0
        i = n-1
        while i >= 0 and not s[i].isalpha():
            i -= 1

        while i >= 0 and s[i] != ' ':
            cnt += 1
            i -= 1

        return cnt

s = Solution()

str = "Hello World"

str = "   fly me   to   the moon  "

str = "luffy is still joyboy"

print(s.lengthOfLastWord(str))

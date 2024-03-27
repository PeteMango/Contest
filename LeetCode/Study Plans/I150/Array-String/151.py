class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')

        ret = ""
        words.reverse()

        for word in words:
            if word.strip() != '':
                ret += word.strip() + " "

        return ret.strip()

s = Solution()

str = "the sky is blue"

str = "  hello world  "

str = "a good   example"

print(s.reverseWords(str))

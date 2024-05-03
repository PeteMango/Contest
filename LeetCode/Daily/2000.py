# Wed, May 1, 2024

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ret = ""
        for i, c in enumerate(word):
            ret += c
            if c == ch:
                print(f'ret is {ret}')
                return ret[::-1] + word[i+1:]
        
        return word
        
s = Solution()

word = "abcdefd"
ch = "d"

word = "xyxzxe"
ch = "z"

word = "abcd"
ch = "z"

print(s.reversePrefix(word, ch))
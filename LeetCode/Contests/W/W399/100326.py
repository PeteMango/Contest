class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        while word:
            c = word[0]
            prefix_length = 0
            while prefix_length < min(9,len(word)) and word[prefix_length] == c:
                prefix_length += 1
            comp += str(prefix_length) + c
            word = word[prefix_length:]
        return comp

s = Solution()

word = "abcde"

word = "aaaaaaaaaaaaaabb"

print(s.compressedString(word))
